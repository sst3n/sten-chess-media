"""Sten Chess long-form (16:9) renderer with the same quality gate ideas as make_short.

spec = {
  "title": str, "intro": [segments], "outro": [segments],
  "chapters": [ {"name": str, "side": "White"|"Black", "segments": [ {say, caption, moves[], arrows[[a,b]], banner,
                  expect_mate, fen, reset} ]} ]
}
Every chapter starts from the initial position. The right-hand panel shows chapter number, name,
caption text and the move list so far, so nothing ever covers the board.
"""
import chess, chess.svg, json, sys, os, shutil, subprocess
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw
import make_short as ms

W, H = 1920, 1080
BOARD = 960
PX, PW = 1080, 780          # right panel x and width
F, BOLD, REG = ms.F, ms.BOLD, ms.REG
BG, GOLD, WHITE, RED, GREY = ms.BG, ms.GOLD, ms.WHITE, ms.RED, ms.GREY
SR = ms.SR
d0 = ImageDraw.Draw(Image.new("RGB", (10, 10)))


def lines(text, size, bold=True):
    return ms.wrap(text, F(BOLD if bold else REG, size), PW)


def movelist(board):
    b = board.root(); out = []
    for i, mv in enumerate(board.move_stack):
        san = b.san(mv)
        if b.turn == chess.WHITE: out.append(f"{b.fullmove_number}.{san}")
        elif i == 0: out.append(f"{b.fullmove_number}...{san}")
        else: out.append(san)
        b.push(mv)
    return " ".join(out)


def validate(spec):
    errs = []
    allsegs = [("intro", s, None) for s in spec.get("intro", [])]
    for ci, ch in enumerate(spec["chapters"]):
        if len(lines(ch["name"], 64)) > 2: errs.append(f"ch{ci} name too long")
        allsegs += [(f"ch{ci}", s, ci) for s in ch["segments"]]
    allsegs += [("outro", s, None) for s in spec.get("outro", [])]
    board, cur = chess.Board(), object()
    for tag, seg, ci in allsegs:
        if ci != cur: board, cur = chess.Board(), ci
        if seg.get("reset"): board = chess.Board()
        if seg.get("fen"): board = chess.Board(seg["fen"])
        if seg.get("caption") and len(lines(seg["caption"], 46)) > 4: errs.append(f"{tag} caption >4 lines: {seg['caption']!r}")
        if seg.get("banner") and len(seg["banner"]) > 24: errs.append(f"{tag} banner too long")
        if len(seg["say"]) > 420: errs.append(f"{tag} narration too long")
        for san in seg.get("moves", []):
            try: board.push(board.parse_san(san))
            except Exception as e: errs.append(f"{tag} illegal {san} after {movelist(board)}: {e}"); return errs
        for a, b in seg.get("arrows", []): chess.parse_square(a); chess.parse_square(b)
        if seg.get("expect_mate") and not board.is_checkmate(): errs.append(f"{tag} claims mate but isn't")
        if board.is_checkmate() and not seg.get("expect_mate") and seg.get("moves"): errs.append(f"{tag} unflagged mate")
    return errs


def frame(chnum, chname, side, board, caption, last=None, arrows=(), check=None, banner=None, bcol=GOLD, flip=False):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    bp = ms.board_png(board, last, arrows, check, flip).resize((BOARD, BOARD), Image.LANCZOS)
    im.paste(bp, (60, 60))
    y = 70
    if chnum:
        d.text((PX, y), f"#{chnum}", font=F(BOLD, 110), fill=GOLD);
        if side:
            tag = side; tw = d.textlength(tag, font=F(BOLD, 34))
            d.rounded_rectangle([PX + PW - tw - 40, y + 30, PX + PW, y + 84], 12, fill=(40, 40, 46))
            d.text((PX + PW - tw - 20, y + 38), tag, font=F(BOLD, 34), fill=WHITE)
        y += 140
    for ln in lines(chname, 64):
        d.text((PX, y), ln, font=F(BOLD, 64), fill=WHITE); y += 78
    y += 20
    d.line([PX, y, PX + PW, y], fill=(60, 60, 66), width=3); y += 30
    if banner:
        bs = 72
        while d.textlength(banner, font=F(BOLD, bs)) > PW - 40: bs -= 4
        d.rounded_rectangle([PX, y, PX + PW, y + bs + 50], 16, fill=(0, 0, 0))
        d.text((PX + (PW - d.textlength(banner, font=F(BOLD, bs))) / 2, y + 22), banner, font=F(BOLD, bs), fill=bcol)
        y += bs + 80
    if caption:
        for ln in lines(caption, 46):
            d.text((PX, y), ln, font=F(BOLD, 46), fill=GOLD); y += 60
    ml = movelist(board) if board.move_stack else ""
    if ml:
        mls = ms.wrap(ml, F(REG, 36), PW)[-4:]
        yy = 1020 - 48 * len(mls)
        for ln in mls: d.text((PX, yy), ln, font=F(REG, 36), fill=GREY); yy += 48
    d.text((W - 260, 1030), "@stenchess", font=F(BOLD, 30), fill=(90, 90, 100))
    return im


def title_card(big, small, sub=None):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    f1 = F(BOLD, 150)
    w = d.textlength(big, font=f1); d.text(((W - w) / 2, 300), big, font=f1, fill=GOLD)
    y = 500
    for ln in ms.wrap(small, F(BOLD, 96), 1700):
        w = d.textlength(ln, font=F(BOLD, 96)); d.text(((W - w) / 2, y), ln, font=F(BOLD, 96), fill=WHITE); y += 115
    if sub:
        w = d.textlength(sub, font=F(BOLD, 48)); d.text(((W - w) / 2, y + 30), sub, font=F(BOLD, 48), fill=GREY)
    return im


def render(spec, outpath, work="/tmp/long", sheet=None):
    errs = validate(spec)
    if errs: raise ms.QAError("; ".join(errs))
    shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    frames, audio, sfx, keys, chapters = [], [], [], [], []
    t = 0.0

    def add(img, sec, key=False):
        p = f"{work}/f{len(frames):05d}.png"; img.save(p); frames.append((p, sec))
        if key: keys.append(img)

    def run(segs, chnum, chname, side, flip):
        nonlocal t
        board = chess.Board()
        for seg in segs:
            if seg.get("reset"): board = chess.Board()
            if seg.get("fen"): board = chess.Board(seg["fen"])
            voice = ms.tts(seg["say"]); vdur = len(voice) / SR
            moves = seg.get("moves", [])
            dur = max(vdur + 0.45, 1.1 * len(moves) + 0.8)
            audio.append((t, voice))
            cap = seg.get("caption", "")
            arrows = [chess.svg.Arrow(chess.parse_square(a), chess.parse_square(b), color="#e63946cc") for a, b in seg.get("arrows", [])]
            last = board.peek() if board.move_stack else None
            if not moves:
                chk = board.king(board.turn) if board.is_check() else None
                add(frame(chnum, chname, side, board, cap, last, arrows, chk, seg.get("banner"), flip=flip), dur, True)
            else:
                lead = 0.4; step = (dur - lead) / len(moves)
                add(frame(chnum, chname, side, board, cap, last, [], None, seg.get("banner"), flip=flip), lead)
                for i, san in enumerate(moves):
                    mv = board.parse_san(san); board.push(mv)
                    mate = board.is_checkmate(); chk = board.king(board.turn) if board.is_check() else None
                    ban = "CHECKMATE!" if mate else seg.get("banner")
                    add(frame(chnum, chname, side, board, cap, mv, [] if mate else (arrows if i == len(moves) - 1 else []),
                              chk, ban, RED if mate else GOLD, flip=flip), step, i == len(moves) - 1)
                    sfx.append((t + lead + i * step, "mate" if mate else "click"))
            t += dur
            if seg.get("pause"):
                last2 = board.peek() if board.move_stack else None
                chk = board.king(board.turn) if board.is_check() else None
                for k in range(seg["pause"], 0, -1):
                    add(frame(chnum, chname, side, board, "Pause and decide!", last2, arrows, chk, f"{k}...", RED, flip=flip), 1.0, k == seg["pause"])
                    sfx.append((t, "click")); t += 1.0

    run(spec["intro"], None, spec["title"], None, False)
    for ci, ch in enumerate(spec["chapters"]):
        chapters.append((t, f"#{ci+1} {ch['name']}"))
        n = len(spec["chapters"]) - ci
        card = title_card(f"#{ci+1}", ch["name"], ch.get("sub", f"play as {ch['side']}"))
        add(card, 1.6, True); sfx.append((t, "whoosh")); t += 1.6
        run(ch["segments"], ci + 1, ch["name"], ch.get("tag", f"play as {ch['side']}"), ch.get("flip", False))
    ot = spec.get("outro_title", "Which one will you play?")
    chapters.append((t, ot))
    run(spec["outro"], None, ot, None, False)

    n = int((t + 0.6) * SR); mix = np.zeros(n, np.float32); tt = np.arange(n) / SR
    mix += (0.018 * (np.sin(2*np.pi*110*tt) + .6*np.sin(2*np.pi*164.8*tt) + .4*np.sin(2*np.pi*220*tt))).astype(np.float32)
    for st, v in audio:
        o = int(st * SR); mix[o:o + len(v)] += v[:n - o]
    for st, kind in sfx:
        o = int(st * SR)
        if kind == "click": s = ms.click(int(.06 * SR))
        elif kind == "mate": s = ms.chime(int(1.0 * SR))
        else:
            m = int(.5 * SR); x = np.arange(m) / SR
            s = (0.12 * np.sin(2*np.pi*(300 + 900*x)*x) * np.exp(-x / .15)).astype(np.float32)
        mix[o:o + len(s)] += s[:n - o]
    mix /= max(1.0, np.abs(mix).max() / 0.95)
    sf.write(f"{work}/audio.wav", mix, SR)
    with open(f"{work}/list.txt", "w") as f:
        for p, sec in frames: f.write(f"file '{p}'\nduration {sec:.3f}\n")
        f.write(f"file '{frames[-1][0]}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt",
                    "-i", f"{work}/audio.wav", "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast",
                    "-crf", "21", "-tune", "stillimage", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart",
                    outpath], check=True)
    if sheet:
        th = [k.resize((384, 216)) for k in keys]
        cols = 6; rows = (len(th) + cols - 1) // cols
        cs = Image.new("RGB", (384 * cols, 216 * rows), BG)
        for i, k in enumerate(th): cs.paste(k, (384 * (i % cols), 216 * (i // cols)))
        cs.save(sheet)
    return t, chapters


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    if sys.argv[2] == "--check":
        e = validate(spec); print("\n".join(e) or "OK"); sys.exit(1 if e else 0)
    dur, chs = render(spec, sys.argv[2], sheet=sys.argv[3] if len(sys.argv) > 3 else None)
    print(f"duration {dur:.1f}s")
    for st, name in chs: print(f"{int(st)//60}:{int(st)%60:02d} {name}")
