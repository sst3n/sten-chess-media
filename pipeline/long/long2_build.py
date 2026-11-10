import json
S=lambda say,**k: dict(say=say,**k)
def ch(name,segs,flip=False): return {"name":name,"side":"-","tag":"guess first!","sub":"Pause and decide","flip":flip,"segments":segs}
spec={"title":"10 Chess Rules Most Players Get Wrong","outro_title":"What's your score?",
"intro":[S("Ten chess rules that most players get wrong. Keep score: for every position, decide your answer before I reveal it. Let's see how many you get right out of ten.",
  caption="Keep score. Decide before the answer.",banner="10 RULES")],
"chapters":[
 ch("Castling through check",[
  S("The king and rook haven't moved, and the king is not in check. Can White castle?",fen="4k3/8/8/8/2b5/8/8/4K2R w K - 0 1",caption="Can White castle here?"),
  S("No. The bishop attacks f1, and the king may never pass through an attacked square. It also can't castle out of check, or into check.",arrows=[["c4","f1"]],banner="ILLEGAL",caption="Out of, into or THROUGH check"),
  S("But if only the rook is attacked, castling is completely legal.",fen="4k2r/8/8/8/8/8/8/4K2R w K - 0 1",arrows=[["h8","h1"]],caption="Rook attacked = still legal"),
  S("White castles, and the rook escapes at the same time.",moves=["O-O"],caption="Rook attacked = still legal"),
 ]),
 ch("The b1 square",[
  S("Now the queenside. Black's rook attacks b1, a square White's rook has to cross. Can White castle?",fen="1r4k1/8/8/8/8/8/8/R3K3 w Q - 0 1",arrows=[["b8","b1"]],caption="The rook crosses b1..."),
  S("Yes! Only the squares the king walks over matter: e1, d1 and c1. The b1 square doesn't count.",moves=["O-O-O"],banner="LEGAL",caption="Only the KING's squares count"),
 ]),
 ch("The king that came back",[
  S("White's king steps to f1, then walks straight back to e1. Nothing has changed. So can White castle now?",fen="r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1",moves=["Kf1","a6","Ke1","a5"],caption="Can White castle now?"),
  S("No! Once the king has moved, castling is gone for the rest of the game, even if it walks back.",arrows=[["e1","g1"],["e1","c1"]],banner="NO CASTLING",caption="King moved = castling gone"),
  S("But if only a rook moves away and comes back, you lose castling on that side only.",fen="r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1",moves=["Rg1","a6","Rh1","a5"],caption="Rook moved: that side only"),
  S("So White can still castle the other way.",moves=["O-O-O"],caption="Queenside is still OK"),
 ]),
 ch("En passant",[
  S("Black pushes the pawn two squares and lands right next to White's pawn. Can White capture it?",fen="4k3/3p4/8/4P3/8/8/8/4K3 b - - 0 1",moves=["d5"],caption="Can White capture it?"),
  S("Yes! It's called en passant. White captures it as if it had only moved one square.",moves=["exd6"],banner="EN PASSANT",caption="Capture 'in passing'"),
  S("The catch: you can only do it on the very next move. Wait one move and the chance is gone forever.",caption="Only on the very next move"),
 ]),
 ch("Stalemate",[
  S("White is a whole queen up and plays queen g6. Black's king has no moves left. Is that a win?",fen="7k/5K2/8/8/8/8/6Q1/8 w - - 0 1",moves=["Qg6"],caption="Queen g6. Is it a win?"),
  S("No! Black is not in check, but has no legal move. That's stalemate, and the game is a draw.",banner="DRAW",caption="No moves + no check = draw"),
  S("Queen g7 instead is checkmate, because now the king is in check.",fen="7k/5K2/8/8/8/8/6Q1/8 w - - 0 1",moves=["Qg7#"],expect_mate=True,caption="Qg7 is the win"),
 ]),
 ch("Promotion",[
  S("When a pawn reaches the last rank, it can become a queen, rook, bishop or knight. Even a second queen is allowed. But never a king, and it can't stay a pawn.",fen="8/pP6/k1K5/p7/8/8/8/8 w - - 0 1",arrows=[["b7","b8"]],caption="Any piece. Even a 2nd queen."),
  S("And sometimes a queen is the wrong choice. Here a queen isn't even check, but a knight is checkmate.",moves=["b8=N#"],expect_mate=True,caption="Knight = checkmate"),
 ]),
 ch("The pinned knight",[
  S("Black's queen is hanging on d4, and White's knight attacks it. Can White take the queen?",fen="4r1k1/8/8/8/3q4/8/4N3/4K3 w - - 0 1",arrows=[["e2","d4"]],caption="Can the knight take?"),
  S("No! The knight is pinned. If it moves, the rook attacks the king, and you can never put your own king in check.",arrows=[["e8","e1"]],banner="PINNED",caption="Never expose your own king"),
 ]),
 ch("Kings can't touch",[
  S("Can White's king walk to e5, right next to Black's king?",fen="8/8/4k3/8/4K3/8/8/8 w - - 0 1",arrows=[["e4","e5"]],caption="Can the king go to e5?"),
  S("Never. Two kings can never stand next to each other, because each one would be in check.",banner="ILLEGAL",caption="Kings always keep a gap"),
  S("This face-off is called the opposition, and it decides a lot of endgames.",caption="It's called the opposition"),
 ]),
 ch("Not enough to win",[
  S("White has an extra bishop. Can White still win this?",fen="8/8/4k3/8/8/2B5/4K3/8 w - - 0 1",caption="Extra bishop. Can White win?"),
  S("No. King and bishop can't checkmate, so the game is drawn right away. The same goes for king and knight.",banner="DRAW",caption="King + bishop = draw"),
  S("Two knights are different: mate can't be forced, but it's possible if the defender blunders, so the game goes on.",caption="Two knights: the game goes on"),
 ]),
 ch("Capturing the checker",[
  S("White's king is in check from the queen. Can the king simply take it?",fen="4k3/8/8/8/8/8/3q4/4K3 w - - 0 1",caption="Can the king take the queen?"),
  S("Yes! A king can capture any piece that isn't protected.",moves=["Kxd2"],banner="TAKE IT",caption="Unprotected = take it"),
  S("But if a rook protects the queen, taking it would walk into check. The king has to run.",fen="3rk3/8/8/8/8/8/3q4/4K3 w - - 0 1",arrows=[["d8","d2"]],caption="Protected = you can't take"),
  S("Here king f1 is the only legal move.",moves=["Kf1"],caption="The only move: Kf1"),
 ]),
],
"outro":[S("So what's your score out of ten? Write it in the comments, and subscribe for daily chess rules, traps and puzzles.",caption="Comment your score out of 10!",banner="YOUR SCORE?")]}
for c in spec["chapters"]: c["segments"][0]["pause"]=3
json.dump(spec,open("long/long2.json","w"),indent=1)
