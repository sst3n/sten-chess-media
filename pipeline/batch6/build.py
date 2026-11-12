import json
def cta(n): 
    return ({"say":f"Did you know this? Rule number {n+1} drops tomorrow. Subscribe so you don't miss it.","caption":f"Rule #{n+1} tomorrow!"} if n<8
            else {"say":"Did you know this? More rules are coming. Subscribe so you don't miss them.","caption":"Subscribe for more!"})
R={}
R[1]=("b1-square",{"fen":"1r4k1/8/8/8/8/8/8/R3K3 w Q - 0 1","q":"Castle here?","segments":[
 {"say":"Chess rule number one. Black's rook attacks b1, a square White's rook has to cross. Can White castle queenside? Decide now.","arrows":[["b8","b1"]],"caption":"Castle through attacked b1?"},
 {"say":"Yes! Only the squares the king walks over matter: e1, d1 and c1. The b1 square doesn't count.","moves":["O-O-O"],"banner":"LEGAL"}]})
R[2]=("king-came-back",{"fen":"r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1","q":"Castle now?","segments":[
 {"say":"Chess rule number two. White's king steps to f1, then walks straight back. Nothing has changed. Can White castle now?","moves":["Kf1","a6","Ke1","a5"],"caption":"The king went back. Castle?"},
 {"say":"No! Once the king has moved, castling is gone for the rest of the game, even if it walks back.","arrows":[["e1","g1"],["e1","c1"]],"banner":"NO CASTLING"}]})
R[3]=("pinned-knight",{"fen":"4r1k1/8/8/8/3q4/8/4N3/4K3 w - - 0 1","q":"Take the queen?","segments":[
 {"say":"Chess rule number three. Black's queen is hanging, and the knight attacks it. Can White take the queen?","arrows":[["e2","d4"]],"caption":"Free queen?"},
 {"say":"No! The knight is pinned. If it moves, the rook attacks the king, and you can never leave your own king in check.","arrows":[["e8","e1"]],"banner":"PINNED"}]})
R[4]=("kings-cant-touch",{"fen":"8/8/4k3/8/4K3/8/8/8 w - - 0 1","q":"Go to e5?","segments":[
 {"say":"Chess rule number four. Can White's king walk to e5, right next to Black's king?","arrows":[["e4","e5"]],"caption":"Walk up to the other king?"},
 {"say":"Never. Two kings can never stand next to each other, because each one would be in check.","banner":"ILLEGAL"}]})
R[5]=("bishop-draw",{"fen":"8/8/4k3/8/8/2B5/4K3/8 w - - 0 1","q":"Is this a win?","segments":[
 {"say":"Chess rule number five. White has an extra bishop. Can White still win?","caption":"An extra bishop. Win?"},
 {"say":"No. King and bishop can't checkmate, so the game is a draw right away. Same with king and knight.","banner":"DRAW"}]})
R[6]=("take-the-checker",{"fen":"3rk3/8/8/8/8/8/3q4/4K3 w - - 0 1","q":"Take the queen?","segments":[
 {"say":"Chess rule number six. The queen gives check, right next to White's king. Can the king just take it?","caption":"Take the queen?"},
 {"say":"No! The rook protects the queen, and a king can never capture into check. King f1 is the only legal move.","arrows":[["d8","d2"]],"moves":["Kf1"],"banner":"PROTECTED"}]})
R[7]=("pinned-still-attacks",{"fen":"8/8/8/3k4/4b3/8/1N6/K7 b - - 0 1","q":"Go to c4?","segments":[
 {"say":"Chess rule number seven. White's knight is pinned by the bishop. So can Black's king walk to c4, a square the knight covers?","arrows":[["e4","a1"],["d5","c4"]],"caption":"The knight is pinned..."},
 {"say":"No! A pinned piece still attacks. The king can never step onto a square a pinned piece covers.","arrows":[["b2","c4"]],"banner":"STILL ILLEGAL"}]})
R[8]=("perpetual-check",{"fen":"6k1/6p1/8/7Q/8/8/rrq2PPP/6K1 w - - 0 1","q":"Lost or saved?","segments":[
 {"say":"Chess rule number eight. Black is up two whole rooks. Can White still save the game?","caption":"Down two rooks. Saved?"},
 {"say":"Yes! Queen e8 check, queen h5 check, again and again. The king can never escape.","moves":["Qe8+","Kh7","Qh5+","Kg8","Qe8+","Kh7","Qh5+","Kg8"],"banner":"PERPETUAL"},
 {"say":"When the same position appears three times, it's a draw by repetition.","banner":"DRAW"}]})
for n,(slug,s) in R.items():
    segs=s["segments"]+[cta(n)]
    spec={"title":f"Rule #{n}: {s['q']}","fen":s["fen"],"segments":segs}
    json.dump(spec,open(f"batch6/rule{n}-{slug}.json","w"),indent=1)
