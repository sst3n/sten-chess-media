import json
specs={
"28-en-passant":{"title":"Can White take this pawn?","fen":"4k3/3p4/8/4P3/8/8/8/4K3 b - - 0 1","segments":[
 {"say":"Black pushes the pawn two squares, right next to White's pawn. Can White capture it?","moves":["d5"],"caption":"Legal or illegal?"},
 {"say":"Yes! It's called en passant. White captures it as if it had only moved one square.","moves":["exd6"],"banner":"EN PASSANT"},
 {"say":"But here's the catch. You can only do it on the very next move. Wait one move, and the chance is gone forever.","caption":"Only on the very next move"},
 {"say":"Did you know this rule? Comment yes or no.","caption":"Did you know this?"}]},
"29-is-this-checkmate":{"title":"Is this checkmate?","fen":"6k1/3n1ppp/8/8/8/8/5PPP/4R1K1 w - - 0 1","segments":[
 {"say":"White plays rook e8, check. The king is stuck behind its own pawns. Is it checkmate?","moves":["Re8+"],"caption":"Checkmate... right?"},
 {"say":"No! The knight jumps back to f8 and blocks the check.","moves":["Nf8"],"banner":"NOT MATE"},
 {"say":"Before you celebrate, check every block and every capture. That's how won games get thrown away.","caption":"Check blocks AND captures"},
 {"say":"Did you spot the knight? Comment yes or no.","caption":"Did you spot it?"}]},
"30-underpromotion":{"title":"Make a queen? WRONG.","fen":"8/pP6/k1K5/p7/8/8/8/8 w - - 0 1","puzzle":{"mate_in":1},"segments":[
 {"say":"White's pawn is about to promote. Everyone makes a queen, right? Pause and think.","caption":"Queen... or something else?","arrows":[["b7","b8"]]},
 {"say":"A queen isn't even check. Make a knight instead!","moves":["b8=N#"],"expect_mate":True,"caption":"Promote to a KNIGHT"},
 {"say":"The black king is boxed in by its own pawns, and the knight checks it. Checkmate in one.","caption":"Boxed in by its own pawns"},
 {"say":"Would you have made a knight? Comment yes or no.","caption":"Would you have found it?"}]},
}
for k,v in specs.items(): json.dump(v,open(f"batch5/{k}.json","w"),indent=1)
