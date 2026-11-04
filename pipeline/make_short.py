"""Sten Chess Short renderer with a quality gate.

spec = {
  "title": str (must fit on ONE line),
  "fen": optional start FEN, "flip": optional bool (show from Black's side),
  "puzzle": optional {"mate_in": 1|2}  -> solution move must be the UNIQUE winning first move,
  "segments": [ {say, caption (one line), moves[], arrows[[a,b]], banner, expect_mate, expect_captures[], reset, setup[]} ]
}
Banners are drawn in the caption strip ABOVE the board, so they can never hide a piece.
"""
import chess, chess.svg, cairosvg, io, json, sys, subprocess, os, shutil
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BG = (14, 14, 16); GOLD = (244, 190, 40); WHITE = (245, 245, 245); RED = (255, 72, 72); GREY = (150, 150, 160)
VOICE, SPEED, SR = "am_michael", 1.12, 24000
TITLE_PX, CAP_PX = 64, 62
_K = None

def F(p, s): return ImageFont.truetype(p, s)
_meas = ImageDraw.Draw(Image.new("RGB", (10, 10)))
def width(text, path, size): return _meas.textlength(text, font=F(path, size))

class QAError(Exception): pass

# ---------------- chess verification ----------------
def mates_in(board, n):
    """True if side to move can force mate in <= n moves."""
    for mv in list(board.legal_moves):
        board.push(mv)
        if board.is_checkmate(): board.pop(); return True
        ok = False
        if n > 1 and not board.is_game_over():
            ok = all(_after_reply(board, r, n - 1) for r in list(board.legal_moves))
        board.pop()
        if ok: return True
    return False

def _after_reply(board, reply, n):
    board.push(reply); r = mates_in(board, n); board.pop(); return r

def winning_first_moves(board, n):
    wins = []
    for mv in list(board.legal_moves):
        board.push(mv)
        if board.is_checkmate(): wins.append(mv)
        elif n > 1 and not board.is_game_over() and all(_after_reply(board, r, n - 1) for r in list(board.legal_moves)):
            wins.append(mv)
        board.pop()
    return wins

def validate(spec):
    errs = []
    if width(spec["title"], BOLD, TITLE_PX) > 1030: errs.append(f"title too long: {spec['title']!r}")
    board = chess.Board(spec.get("fen", chess.STARTING_FEN))
    if not board.is_valid(): errs.append("start position invalid")
    if "puzzle" in spec:
        n = spec["puzzle"]["mate_in"]
        sol_seg = next((s for s in spec["segments"] if s.get("moves")), None)
        wins = winning_first_moves(board.copy(), n)
        first = board.parse_san(sol_seg["moves"][0]) if sol_seg else None
        if len(wins) != 1 or wins[0] != first:
            errs.append(f"puzzle not unique/correct: winning first moves={[board.san(m) for m in wins]}")
    for i, seg in enumerate(spec["segments"]):
        if seg.get("reset"): board = chess.Board(spec.get("fen", chess.STARTING_FEN))
        if seg.get("fen"): board = chess.Board(seg["fen"])
        cap = seg.get("caption", "")
        if cap and width(cap, BOLD, CAP_PX) > 1000: errs.append(f"seg{i} caption too long: {cap!r}")
        if seg.get("banner") and len(seg["banner"]) > 22: errs.append(f"seg{i} banner too long")
        caps = []
        for san in seg.get("setup", []) + seg.get("moves", []):
            try: mv = board.parse_san(san)
            except Exception as e: errs.append(f"seg{i} illegal move {san}: {e}"); return errs
            if board.is_capture(mv):
                p = board.piece_at(mv.to_square) if not board.is_en_passant(mv) else chess.Piece(chess.PAWN, not board.turn)
                caps.append(p.symbol().lower())
            board.push(mv)
        for a, b in seg.get("arrows", []):
            chess.parse_square(a); chess.parse_square(b)
        if seg.get("expect_mate") and not board.is_checkmate(): errs.append(f"seg{i} claims mate but isn't")
        if not seg.get("expect_mate") and board.is_checkmate() and "CHECKMATE" not in (seg.get("banner") or "").upper() and seg.get("moves"):
            errs.append(f"seg{i} ends in mate but not flagged")
        for c in seg.get("expect_captures", []):
            if c not in caps: errs.append(f"seg{i} claims capture of {c} but captured {caps}")
        if len(seg["say"]) > 260: errs.append(f"seg{i} narration too long")
    return errs

# ---------------- rendering ----------------
def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if _meas.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def ctext(d, y, text, font, fill, maxw=1000):
    for ln in wrap(text, font, maxw):
        w = d.textlength(ln, font=font)
        d.text(((W - w) / 2, y), ln, font=font, fill=fill, stroke_width=4, stroke_fill=(0, 0, 0))
        y += font.size + 12

def board_png(board, last, arrows, check, flip):
    svg = chess.svg.board(board, size=1000, lastmove=last, check=check, arrows=list(arrows), flipped=flip,
                          coordinates=True,
                          colors={"square light": "#eeeed2", "square dark": "#769656",
                                  "square light lastmove": "#f6f669", "square dark lastmove": "#baca2b"})
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert("RGB")

def frame(spec, board, caption, last=None, arrows=(), check=None, banner=None, banner_col=GOLD):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    ctext(d, 190, spec["title"], F(BOLD, TITLE_PX), WHITE, maxw=1040)
    if banner:   # banner lives in the caption strip, never over the board
        d.rectangle([0, 300, W, 470], fill=(0, 0, 0))
        bs = 100
        while bs > 56 and d.textlength(banner, font=F(BOLD, bs)) > 1000: bs -= 4
        ctext(d, 385 - bs // 2 - 6, banner, F(BOLD, bs), banner_col, maxw=1060)
    elif caption:
        ctext(d, 340, caption, F(BOLD, CAP_PX), GOLD)
    im.paste(board_png(board, last, arrows, check, spec.get("flip", False)), (40, 500))
    d.text((40, 1520), "@stenchess", font=F(BOLD, 38), fill=GREY)
    return im

def tts(text):
    global _K
    if _K is None:
        from kokoro_onnx import Kokoro
        _K = Kokoro("/home/claude/tts/kokoro.onnx", "/home/claude/tts/voices.bin")
    s, sr = _K.create(text, voice=VOICE, speed=SPEED, lang="en-us")
    assert sr == SR
    return s.astype(np.float32)

def click(n):
    t = np.arange(n) / SR
    return (0.5 * np.exp(-t / 0.008) * (0.6 * np.sin(2 * np.pi * 900 * t) + 0.4 * (np.random.rand(n) * 2 - 1))).astype(np.float32)

def chime(n):
    out = np.zeros(n, np.float32); t = np.arange(n) / SR
    for f0, dl in ((523.3, 0), (659.3, .08), (784, .16), (1046.5, .24)):
        o = int(dl * SR); out[o:] += (0.16 * np.exp(-t[:n - o] / 0.3) * np.sin(2 * np.pi * f0 * t[:n - o])).astype(np.float32)
    return out

def render(spec, outpath, work="/tmp/short", sheet=None):
    errs = validate(spec)
    if errs: raise QAError("; ".join(errs))
    shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    board = chess.Board(spec.get("fen", chess.STARTING_FEN))
    frames, audio, sfx, keyframes = [], [], [], []
    t = 0.0
    def add(img, sec, key=False):
        p = f"{work}/f{len(frames):04d}.png"; img.save(p); frames.append((p, sec))
        if key: keyframes.append(img)
    for seg in spec["segments"]:
        if seg.get("reset"): board = chess.Board(spec.get("fen", chess.STARTING_FEN))
        if seg.get("fen"): board = chess.Board(seg["fen"])
        for san in seg.get("setup", []): board.push_san(san)
        voice = tts(seg["say"]); vdur = len(voice) / SR
        moves = seg.get("moves", [])
        seg_dur = max(vdur + 0.3, 0.9 * len(moves) + 0.6)
        audio.append((t, voice))
        cap = seg.get("caption", "")
        last = board.peek() if board.move_stack else None
        arrows = [chess.svg.Arrow(chess.parse_square(a), chess.parse_square(b), color="#e63946cc") for a, b in seg.get("arrows", [])]
        if not moves:
            chk = board.king(board.turn) if board.is_check() else None
            add(frame(spec, board, cap, last, arrows, chk, seg.get("banner"), RED if board.is_checkmate() else GOLD), seg_dur, True)
        else:
            lead = 0.35; step = (seg_dur - lead) / len(moves)
            add(frame(spec, board, cap, last, arrows, None, seg.get("banner")), lead)
            for i, san in enumerate(moves):
                mv = board.parse_san(san); board.push(mv)
                mate = board.is_checkmate(); chk = board.king(board.turn) if board.is_check() else None
                ban = "CHECKMATE!" if mate else seg.get("banner")
                add(frame(spec, board, cap, mv, [] if mate else arrows, chk, ban, RED if mate else GOLD), step, i == len(moves) - 1)
                sfx.append((t + lead + i * step, "mate" if mate else "click"))
        t += seg_dur
    n = int((t + 0.5) * SR); mix = np.zeros(n, np.float32); tt = np.arange(n) / SR
    mix += (0.022 * (np.sin(2*np.pi*110*tt) + .6*np.sin(2*np.pi*164.8*tt) + .4*np.sin(2*np.pi*220*tt))).astype(np.float32)
    for st, v in audio:
        o = int(st * SR); mix[o:o + len(v)] += v[:n - o]
    for st, kind in sfx:
        o = int(st * SR); s = click(int(.06 * SR)) if kind == "click" else chime(int(1.0 * SR))
        mix[o:o + len(s)] += s[:n - o]
    mix /= max(1.0, np.abs(mix).max() / 0.95)
    sf.write(f"{work}/audio.wav", mix, SR)
    with open(f"{work}/list.txt", "w") as f:
        for p, sec in frames: f.write(f"file '{p}'\nduration {sec:.3f}\n")
        f.write(f"file '{frames[-1][0]}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt",
                    "-i", f"{work}/audio.wav", "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast",
                    "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", outpath], check=True)
    if sheet:  # contact sheet of key frames for visual review
        th = [k.resize((216, 384)) for k in keyframes]
        cs = Image.new("RGB", (216 * len(th), 384), BG)
        for i, k in enumerate(th): cs.paste(k, (216 * i, 0))
        cs.save(sheet)
    return t

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    print(f"rendered {sys.argv[2]} {render(spec, sys.argv[2], sheet=sys.argv[3] if len(sys.argv) > 3 else None):.1f}s")
