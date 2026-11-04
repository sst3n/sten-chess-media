"""Batch 2: 19 Shorts (09-27). Each entry: spec (for renderer) + YouTube metadata."""
import json, os
S = []
def add(slug, spec, yt_title, desc, tags):
    S.append({"slug": slug, "spec": spec, "yt_title": yt_title, "desc": desc, "tags": tags})

FOLLOW = "Follow @stenchess for a new chess trick every day."

# 09 Stafford Gambit trap
add("stafford-trap", {"title": "This trap wins in 8 moves", "segments": [
  {"say": "This opening trap catches thousands of players every single day.", "caption": "The Stafford trap"},
  {"say": "White takes the pawn. Black ignores it and plays knight c6.", "moves": ["e4","e5","Nf3","Nf6","Nxe5","Nc6"], "caption": "Black gives a pawn"},
  {"say": "White grabs the knight. Black recaptures, opening lines for the bishop and queen.", "moves": ["Nxc6","dxc6"], "caption": "Lines open up"},
  {"say": "d3, bishop c5. Now White pins the knight with bishop g5. Looks great.", "moves": ["d3","Bc5","Bg5"], "caption": "Looks great for White..."},
  {"say": "But Black takes on e4 and gives away the queen!", "moves": ["Nxe4"], "caption": "Queen sacrifice!"},
  {"say": "Bishop takes the queen. Then bishop takes f2, check. King e2. And bishop g4. Checkmate.", "moves": ["Bxd8","Bxf2+","Ke2","Bg4#"], "expect_mate": True, "caption": "Bishop g4 mate"},
  {"say": "Black gave up the queen and still won. Save this for your next game.", "caption": "Save this trap"}]},
  "Black gives up the QUEEN and still wins 😱 #chess",
  "The Stafford Gambit trap: Black sacrifices the queen and checkmates with two bishops.\n\nThe line: 1.e4 e5 2.Nf3 Nf6 3.Nxe5 Nc6 4.Nxc6 dxc6 5.d3 Bc5 6.Bg5?? Nxe4! 7.Bxd8 Bxf2+ 8.Ke2 Bg4#\n\nWould you have taken the queen? Comment below 👇\n" + FOLLOW + "\n\n#chess #staffordgambit #chesstraps #checkmate #shorts",
  ["chess", "stafford gambit", "chess trap", "queen sacrifice", "checkmate"])

# 10 Philidor's legacy (smothered mate in 2)
add("smothered-mate-in-2", {"title": "Mate in 2. Find it.", "fen": "r6k/6pp/7N/8/8/1Q6/8/6K1 w - - 0 1", "puzzle": {"mate_in": 2}, "segments": [
  {"say": "White to move and checkmate in two. The first move looks completely crazy.", "caption": "White to move: mate in 2"},
  {"say": "Pause the video. Look at the knight and the corner king.", "banner": "PAUSE & FIND IT"},
  {"say": "Queen g8, check! A full queen sacrifice.", "moves": ["Qg8+"], "caption": "Queen g8!!"},
  {"say": "The king can't take, because the knight protects g8. So the rook must take.", "moves": ["Rxg8"], "caption": "Rook is forced to take"},
  {"say": "Knight f7. Checkmate. The king is buried by its own pieces.", "moves": ["Nf7#"], "expect_mate": True, "caption": "Smothered mate"},
  {"say": "Did you see the queen sacrifice? Comment how fast you found it.", "caption": "How fast did YOU see it?"}]},
  "Sacrifice the QUEEN, mate in 2 ♞ Smothered mate #chesspuzzle",
  "White to move and mate in 2. Pause and find it! ♞\n\nAnswer: 1.Qg8+!! Rxg8 2.Nf7# - the famous SMOTHERED MATE. The king can't take the queen because the knight guards g8.\n\nHow fast did you see it? 👇\n" + FOLLOW + "\n\n#chess #chesspuzzle #smotheredmate #queensacrifice #shorts",
  ["chess", "chess puzzle", "smothered mate", "mate in 2", "queen sacrifice"])

# 11 Opera Game
add("opera-game", {"title": "Most famous chess game", "segments": [
  {"say": "Paris, 1858. Paul Morphy plays this game at the opera house, and it's still taught to beginners today.", "caption": "Morphy, Paris 1858"},
  {"say": "Morphy develops fast and sacrifices pieces to open lines to the black king.", "setup": ["e4","e5","Nf3","d6","d4","Bg4","dxe5","Bxf3","Qxf3","dxe5","Bc4","Nf6","Qb3","Qe7","Nc3","c6","Bg5","b5","Nxb5","cxb5","Bxb5+","Nbd7","O-O-O","Rd8"], "caption": "Every piece attacking"},
  {"say": "Rook takes d7. Rook takes back. Another rook joins the attack.", "moves": ["Rxd7","Rxd7","Rd1","Qe6"], "caption": "Rook sacrifice"},
  {"say": "Bishop takes d7, check. Knight takes back. And now the queen sacrifice: queen b8, check!", "moves": ["Bxd7+","Nxd7","Qb8+"], "caption": "Queen b8!!"},
  {"say": "The knight has to take. Rook d8. Checkmate.", "moves": ["Nxb8","Rd8#"], "expect_mate": True, "caption": "Rook d8 mate"},
  {"say": "Fast development and open lines win games. Would you play like Morphy?", "caption": "Could YOU play like this?"}]},
  "The most famous chess game ever ♟️ Morphy's Opera Game #chess",
  "Paul Morphy vs the Duke of Brunswick and Count Isouard - played at the Paris Opera in 1858.\n\nMorphy develops fast, sacrifices a rook and then his QUEEN, and finishes with 17.Rd8#.\n\nWould you play like Morphy? 👇\n" + FOLLOW + "\n\n#chess #operagame #paulmorphy #chesshistory #shorts",
  ["chess", "opera game", "paul morphy", "famous chess games", "queen sacrifice"])

# 12 Castling rules
add("castling-rule", {"title": "Can White castle here?", "fen": "4k3/8/8/8/2b5/8/8/4K2R w K - 0 1", "segments": [
  {"say": "The king and rook haven't moved. The king isn't in check. So can White castle?", "caption": "Legal or illegal?"},
  {"say": "No! The bishop attacks f1, and the king is not allowed to pass through an attacked square.", "arrows": [["c4","f1"]], "banner": "ILLEGAL"},
  {"say": "But here's the weird part. In this position, Black's rook attacks the white rook on h1.", "fen": "4k2r/8/8/8/8/8/8/4K2R w Kk - 0 1", "arrows": [["h8","h1"]], "caption": "But watch this..."},
  {"say": "White can still castle! Only the king's squares matter, not the rook's.", "moves": ["O-O"], "caption": "Rook attacked = OK"},
  {"say": "Did you know this rule? Comment yes or no.", "caption": "Did you know this?"}]},
  "Can you castle here? 🤔 Most players get this rule wrong #chess",
  "The king and rook haven't moved and the king isn't in check... but White still CAN'T castle.\n\nRule: the king can't castle out of check, into check, or THROUGH an attacked square. But if only the rook is attacked, castling is legal!\n\nDid you know this? 👇\n" + FOLLOW + "\n\n#chess #chessrules #castling #chesstips #shorts",
  ["chess", "chess rules", "castling", "chess tips", "beginner chess"])

# 13 Blackburne Shilling trap
add("blackburne-shilling", {"title": "The trap that cost a shilling", "segments": [
  {"say": "Black plays knight d4 and leaves the e5 pawn hanging. It's bait.", "moves": ["e4","e5","Nf3","Nc6","Bc4","Nd4"], "caption": "Free pawn?"},
  {"say": "White takes it. Black's queen jumps to g5, attacking g2.", "moves": ["Nxe5","Qg5"], "arrows": [["g5","g2"]], "caption": "Queen g5!"},
  {"say": "White takes f7, forking queen and rook. Feels winning. Queen takes g2.", "moves": ["Nxf7","Qxg2"], "caption": "Greedy knight"},
  {"say": "Rook f1. Queen takes e4, check. Bishop blocks.", "moves": ["Rf1","Qxe4+","Be2"], "caption": "Check!"},
  {"say": "Knight f3. Checkmate.", "moves": ["Nf3#"], "expect_mate": True, "caption": "Smothered!"},
  {"say": "It's called the Blackburne Shilling trap. Tag a friend who grabs free pawns.", "caption": "Tag a pawn grabber"}]},
  "Never take this FREE pawn 😈 Blackburne Shilling trap #chess",
  "The Blackburne Shilling Gambit trap: Black leaves a pawn hanging, and White's greed gets punished.\n\nThe line: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Nd4 4.Nxe5? Qg5 5.Nxf7?? Qxg2 6.Rf1 Qxe4+ 7.Be2 Nf3#\n\nTag a friend who grabs free pawns 👇\n" + FOLLOW + "\n\n#chess #chesstraps #blackburne #checkmate #shorts",
  ["chess", "chess trap", "blackburne shilling", "opening trap", "checkmate"])

# 14 Arabian mate
add("arabian-mate", {"title": "Rook + knight = checkmate", "fen": "7k/1R6/5N2/8/8/8/8/6K1 w - - 0 1", "puzzle": {"mate_in": 1}, "segments": [
  {"say": "White to move. Checkmate in one with the rook and knight.", "caption": "White to move: mate in 1"},
  {"say": "Pause and find it.", "banner": "3... 2... 1..."},
  {"say": "Rook h7. Checkmate. The knight protects the rook and covers g8.", "moves": ["Rh7#"], "expect_mate": True, "caption": "Rook h7!"},
  {"say": "This is the Arabian mate, one of the oldest checkmate patterns ever recorded. Did you get it?", "caption": "Did YOU find it?"}]},
  "Rook + knight checkmate ♟️ The Arabian Mate #chesspuzzle",
  "White to move: mate in 1. Pause and find it!\n\nAnswer: Rh7# - the knight on f6 protects the rook and covers g8. This is the ARABIAN MATE, one of the oldest recorded checkmate patterns.\n\nDid you get it? 👇\n" + FOLLOW + "\n\n#chess #chesspuzzle #arabianmate #checkmate #shorts",
  ["chess", "chess puzzle", "arabian mate", "mate in 1", "checkmate patterns"])

# 15 Englund Gambit trap
add("englund-trap", {"title": "The queen walks to c1", "segments": [
  {"say": "Against d4, Black throws a pawn away with e5. White takes.", "moves": ["d4","e5","dxe5","Nc6","Nf3","Qe7"], "caption": "Weird opening..."},
  {"say": "White defends the pawn with bishop f4. Queen b4, check.", "moves": ["Bf4","Qb4+"], "caption": "Queen check"},
  {"say": "Bishop blocks. Queen grabs b2.", "moves": ["Bd2","Qxb2"], "caption": "Queen goes deep"},
  {"say": "White attacks the queen with bishop c3. Black calmly plays bishop b4.", "moves": ["Bc3","Bb4"], "caption": "Pin!"},
  {"say": "Queen d2. Bishop takes c3. Queen takes back. And queen c1. Checkmate.", "moves": ["Qd2","Bxc3","Qxc3","Qc1#"], "expect_mate": True, "caption": "Queen c1 mate"},
  {"say": "The Englund Gambit trap. Would you have seen it coming?", "caption": "Would you see it?"}]},
  "The queen walks ALL the way to c1 👑 Englund Gambit trap #chess",
  "The Englund Gambit trap: Black's queen goes deep into White's camp and delivers checkmate on c1.\n\nThe line: 1.d4 e5 2.dxe5 Nc6 3.Nf3 Qe7 4.Bf4 Qb4+ 5.Bd2 Qxb2 6.Bc3? Bb4 7.Qd2 Bxc3 8.Qxc3 Qc1#\n\nWould you have seen it? 👇\n" + FOLLOW + "\n\n#chess #englundgambit #chesstraps #checkmate #shorts",
  ["chess", "englund gambit", "chess trap", "opening trap", "checkmate"])

# 16 Family fork
add("family-fork", {"title": "Knight attacks EVERYTHING", "fen": "r3k3/8/4q3/1N6/8/8/8/6K1 w - - 0 1", "segments": [
  {"say": "White to move. One knight jump attacks the king, the queen and the rook at once.", "caption": "Find the knight jump"},
  {"say": "Pause and find it.", "banner": "3... 2... 1..."},
  {"say": "Knight c7, check! King, queen and rook are all attacked.", "moves": ["Nc7+"], "arrows": [["c7","e8"],["c7","e6"],["c7","a8"]], "caption": "Knight c7!"},
  {"say": "The king must move. And the knight eats the queen.", "moves": ["Kd7","Nxe6"], "expect_captures": ["q"], "caption": "Bye bye queen"},
  {"say": "This is called a family fork. Comment if you found it.", "banner": "FAMILY FORK"}]},
  "One knight attacks EVERYTHING 🐴 Family Fork #chesspuzzle",
  "White to move: one knight jump attacks the king, queen AND rook.\n\nAnswer: Nc7+! The king must move, and the knight takes the queen. This is called a FAMILY FORK.\n\nDid you find it? 👇\n" + FOLLOW + "\n\n#chess #chesspuzzle #knightfork #chesstactics #shorts",
  ["chess", "chess puzzle", "knight fork", "family fork", "chess tactics"])

# 17 Reti vs Tartakower
add("reti-tartakower", {"title": "Queen sac, mate in 3 moves", "segments": [
  {"say": "Vienna, 1910. Réti against Tartakower. Black just grabbed a knight in the center.", "setup": ["e4","c6","d4","d5","Nc3","dxe4","Nxe4","Nf6","Qd3","e5","dxe5","Qa5+","Bd2","Qxe5","O-O-O","Nxe4"], "caption": "Black looks fine"},
  {"say": "Réti plays queen d8, check! Giving away the queen.", "moves": ["Qd8+"], "caption": "Queen d8!!"},
  {"say": "The king has to take.", "moves": ["Kxd8"], "caption": "Forced"},
  {"say": "Bishop g5. Double check! The bishop and the rook both attack the king.", "moves": ["Bg5+"], "caption": "Double check!"},
  {"say": "King c7. And bishop d8. Checkmate.", "moves": ["Kc7","Bd8#"], "expect_mate": True, "caption": "Bishop d8 mate"},
  {"say": "One of the most beautiful finishes in chess history. Would you have seen the queen sac?", "caption": "Would YOU see it?"}]},
  "Queen sacrifice, then DOUBLE CHECK ⚡ Réti vs Tartakower 1910 #chess",
  "Réti vs Tartakower, Vienna 1910 - one of the most famous finishes in chess.\n\n9.Qd8+!! Kxd8 10.Bg5++ (double check!) Kc7 11.Bd8#\n\nWould you have seen the queen sacrifice? 👇\n" + FOLLOW + "\n\n#chess #chesshistory #queensacrifice #doublecheck #shorts",
  ["chess", "reti tartakower", "queen sacrifice", "double check", "famous chess games"])

# 18 Stalemate trap
add("stalemate-trap", {"title": "Win or draw? One move", "fen": "7k/8/5K2/8/8/8/8/6Q1 w - - 0 1", "segments": [
  {"say": "White has a whole queen. One move wins instantly. But one move throws the win away.", "caption": "Win or draw?"},
  {"say": "Watch this mistake. Queen g6.", "moves": ["Qg6"], "caption": "The beginner move..."},
  {"say": "Black isn't in check, but has no legal moves. That's stalemate. A draw!", "banner": "STALEMATE"},
  {"say": "The right move was queen g7. Protected by the king. Checkmate.", "reset": True, "moves": ["Qg7#"], "expect_mate": True, "caption": "Queen g7 wins"},
  {"say": "Always check that the king has a move. Have you ever stalemated someone by accident?", "caption": "Ever done this by accident?"}]},
  "Winning with a QUEEN... and it's a DRAW 😭 #chess",
  "White has a whole extra queen. Qg7 is checkmate - but Qg6?? is STALEMATE and the game is a draw!\n\nStalemate = no legal moves while NOT in check. Always leave the enemy king a move until you can mate.\n\nEver stalemated someone by accident? 👇\n" + FOLLOW + "\n\n#chess #stalemate #chessrules #chesstips #shorts",
  ["chess", "stalemate", "chess rules", "chess mistakes", "beginner chess"])

# 19 Siberian trap
add("siberian-trap", {"title": "The Siberian trap", "segments": [
  {"say": "The Smith Morra Gambit. White gives two pawns for fast development.", "moves": ["e4","c5","d4","cxd4","c3","dxc3","Nxc3","Nc6","Nf3","e6"], "caption": "Gambit opening"},
  {"say": "Bishop c4. Queen c7. White castles. Knight f6. Queen e2.", "moves": ["Bc4","Qc7","O-O","Nf6","Qe2"], "caption": "Normal moves..."},
  {"say": "Knight g4, eyeing h2. White kicks it with h3.", "moves": ["Ng4","h3"], "arrows": [["g4","h2"]], "caption": "Kick the knight?"},
  {"say": "But knight d4! Attacking the queen.", "moves": ["Nd4"], "caption": "Knight d4!"},
  {"say": "White takes the knight. And queen h2. Checkmate.", "moves": ["Nxd4","Qh2#"], "expect_mate": True, "caption": "Queen h2 mate"},
  {"say": "This is the Siberian trap. Save it if you play the Sicilian.", "caption": "Save this trap"}]},
  "The Siberian trap ❄️ Checkmate on h2 #chess",
  "The Siberian trap in the Smith-Morra Gambit.\n\nThe line: 1.e4 c5 2.d4 cxd4 3.c3 dxc3 4.Nxc3 Nc6 5.Nf3 e6 6.Bc4 Qc7 7.O-O Nf6 8.Qe2 Ng4 9.h3?? Nd4! 10.Nxd4 Qh2#\n\nSave it if you play the Sicilian 👇\n" + FOLLOW + "\n\n#chess #siberiantrap #sicilian #chesstraps #shorts",
  ["chess", "siberian trap", "sicilian defense", "smith morra", "chess trap"])

# 20 Boden's mate
add("bodens-mate", {"title": "Two bishops = checkmate", "fen": "2kr4/p2n4/8/8/5B2/8/4B3/6K1 w - - 0 1", "puzzle": {"mate_in": 1}, "segments": [
  {"say": "White to move. The two bishops can checkmate in one move.", "caption": "White to move: mate in 1"},
  {"say": "Pause and find it.", "banner": "3... 2... 1..."},
  {"say": "Bishop a6. Checkmate. The two bishops cross like scissors.", "moves": ["Ba6#"], "expect_mate": True, "arrows": [], "caption": "Bishop a6!"},
  {"say": "This is Boden's mate. The black king is trapped by its own knight and rook. Did you find it?", "caption": "Did YOU find it?"}]},
  "Two bishops, one CHECKMATE ✂️ Boden's Mate #chesspuzzle",
  "White to move: mate in 1. Pause and find it!\n\nAnswer: Ba6# - the two bishops cross like scissors and the king is trapped by its own pieces. This is BODEN'S MATE.\n\nDid you get it? 👇\n" + FOLLOW + "\n\n#chess #chesspuzzle #bodensmate #checkmate #shorts",
  ["chess", "chess puzzle", "bodens mate", "mate in 1", "bishop checkmate"])

# 21 Caro-Kann smothered
add("caro-kann-trap", {"title": "Checkmate in 6 moves", "segments": [
  {"say": "This checkmate happens in only six moves, and it catches real players.", "caption": "6-move checkmate"},
  {"say": "The Caro-Kann. White grabs the center. Black takes on e4.", "moves": ["e4","c6","d4","d5","Nc3","dxe4","Nxe4","Nd7"], "caption": "Caro-Kann"},
  {"say": "White sets a trap with queen e2. Black plays the natural knight f6.", "moves": ["Qe2","Ngf6"], "caption": "Natural move?"},
  {"say": "Knight d6. Checkmate. The king can't move, because its own pieces block every square.", "moves": ["Nd6#"], "expect_mate": True, "caption": "Knight d6 mate"},
  {"say": "A smothered mate in the opening. Have you ever fallen for this?", "caption": "Ever fallen for it?"}]},
  "Checkmate in 6 moves 😳 Caro-Kann smothered mate #chess",
  "A smothered mate in just 6 moves - and it really happens in online games.\n\nThe line: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Qe2 Ngf6?? 6.Nd6#\n\nThe e7 pawn is pinned by the queen, so it can't take the knight.\n\nEver fallen for this? 👇\n" + FOLLOW + "\n\n#chess #carokann #chesstraps #smotheredmate #shorts",
  ["chess", "caro kann", "chess trap", "smothered mate", "6 move checkmate"])

# 22 Fact: 400 positions
add("400-positions", {"title": "How many first moves?", "segments": [
  {"say": "How many different first moves does White have? Take a guess.", "caption": "Guess the number"},
  {"say": "Twenty. Sixteen pawn moves, and four knight moves.", "banner": "20 MOVES"},
  {"say": "After both players make one move, there are already four hundred possible positions.", "banner": "400 POSITIONS"},
  {"say": "And the number of possible chess games is estimated to be bigger than the number of atoms in the observable universe.", "caption": "More than atoms?!"},
  {"say": "What was your guess? Comment below.", "caption": "What was YOUR guess?"}]},
  "Only 20 first moves... then it EXPLODES 🤯 #chess",
  "White has exactly 20 legal first moves: 16 pawn moves and 4 knight moves. After one move each, there are already 400 possible positions.\n\nThe number of possible chess games is estimated (the Shannon number, about 10^120) to be bigger than the number of atoms in the observable universe (about 10^80).\n\nWhat was your guess? 👇\n" + FOLLOW + "\n\n#chess #chessfacts #shannonnumber #funfacts #shorts",
  ["chess", "chess facts", "shannon number", "fun facts", "chess math"])

# 23 Epaulette mate
add("epaulette-mate", {"title": "Trapped by his own rooks", "fen": "3rkr2/8/8/8/8/1Q6/8/6K1 w - - 0 1", "puzzle": {"mate_in": 1}, "segments": [
  {"say": "White to move. Black's rooks are protecting the king... or are they?", "caption": "White to move: mate in 1"},
  {"say": "Pause and find it.", "banner": "3... 2... 1..."},
  {"say": "Queen e6. Checkmate. The rooks block the king's escape squares.", "moves": ["Qe6#"], "expect_mate": True, "caption": "Queen e6!"},
  {"say": "This is the epaulette mate, because the rooks sit on the king's shoulders. Did you find it?", "caption": "Did YOU find it?"}]},
  "Trapped by his OWN rooks 🤦 Epaulette Mate #chesspuzzle",
  "White to move: mate in 1. Pause and find it!\n\nAnswer: Qe6# - the black rooks on d8 and f8 block the king's escape. It's called the EPAULETTE MATE because the rooks sit on the king's shoulders.\n\nDid you find it? 👇\n" + FOLLOW + "\n\n#chess #chesspuzzle #epaulettemate #checkmate #shorts",
  ["chess", "chess puzzle", "epaulette mate", "mate in 1", "checkmate patterns"])

# 24 Lasker king hunt
add("king-hunt", {"title": "The king walks to his death", "segments": [
  {"say": "London, 1912. Edward Lasker plays one of the craziest king hunts ever.", "setup": ["d4","e6","Nf3","f5","Nc3","Nf6","Bg5","Be7","Bxf6","Bxf6","e4","fxe4","Nxe4","b6","Ne5","O-O","Bd3","Bb7","Qh5","Qe7"], "caption": "Lasker vs Thomas, 1912"},
  {"say": "Queen takes h7, check! The king must take.", "moves": ["Qxh7+","Kxh7"], "caption": "Queen sacrifice!"},
  {"say": "Now every white move is a check, and the king gets pulled across the board.", "moves": ["Nxf6+","Kh6","Neg4+","Kg5","h4+","Kf4","g3+","Kf3"], "caption": "Check after check"},
  {"say": "Bishop e2, check. King g2. Rook h2, check. King g1.", "moves": ["Be2+","Kg2","Rh2+","Kg1"], "caption": "All the way to g1"},
  {"say": "And the king steps to d2. Checkmate.", "moves": ["Kd2#"], "expect_mate": True, "caption": "King d2 mate!"},
  {"say": "The black king walked from g8 to g1. Have you ever seen a king hunt like this?", "caption": "Craziest king walk?"}]},
  "The king walks ACROSS the board to his death 💀 #chess",
  "Edward Lasker vs George Thomas, London 1912 - the most famous king hunt in chess.\n\n11.Qxh7+!! Kxh7 and then check after check drags the black king from g8 all the way to g1, finished by 18.Kd2#.\n\nEver seen anything like it? 👇\n" + FOLLOW + "\n\n#chess #kinghunt #chesshistory #queensacrifice #shorts",
  ["chess", "king hunt", "edward lasker", "famous chess games", "queen sacrifice"])

# 25 Skewer
add("skewer", {"title": "Check... bye bye queen", "fen": "q7/8/2k5/8/8/8/8/4KB2 w - - 0 1", "segments": [
  {"say": "White to move. The black king and queen are standing on the same diagonal.", "caption": "Spot the line"},
  {"say": "Bishop g2. Check!", "moves": ["Bg2+"], "arrows": [["g2","a8"]], "caption": "Bishop g2, check!"},
  {"say": "The king has to step off the diagonal. And the bishop takes the queen.", "moves": ["Kc5","Bxa8"], "expect_captures": ["q"], "caption": "Free queen"},
  {"say": "This is called a skewer. Attack the big piece, win the piece behind it.", "banner": "SKEWER"},
  {"say": "Did you know this tactic? Comment yes or no.", "caption": "Did you know it?"}]},
  "Check... and the QUEEN is gone 🍢 The Skewer #chess",
  "The black king and queen are on the same diagonal. Bg2+! The king must move, and Bxa8 wins the queen.\n\nThis is a SKEWER: attack the more valuable piece, win the one behind it.\n\nDid you know this tactic? 👇\n" + FOLLOW + "\n\n#chess #skewer #chesstactics #chesstips #shorts",
  ["chess", "skewer", "chess tactics", "win the queen", "beginner chess"])

# 26 Anastasia's mate
add("anastasias-mate", {"title": "Knight + rook corner mate", "fen": "5r2/4Nppk/8/8/8/8/8/K2R4 w - - 0 1", "puzzle": {"mate_in": 1}, "segments": [
  {"say": "White to move. Checkmate in one move.", "caption": "White to move: mate in 1"},
  {"say": "Pause and find it.", "banner": "3... 2... 1..."},
  {"say": "Rook h1. Checkmate. The knight on e7 covers both escape squares.", "moves": ["Rh1#"], "expect_mate": True, "caption": "Rook h1!"},
  {"say": "This is Anastasia's mate. The black king is stuck behind its own pawn. Did you find it?", "caption": "Did YOU find it?"}]},
  "Knight + rook corner checkmate ♞ Anastasia's Mate #chesspuzzle",
  "White to move: mate in 1. Pause and find it!\n\nAnswer: Rh1# - the knight on e7 covers g6 and g8, and the king is stuck behind its own g7 pawn. This is ANASTASIA'S MATE.\n\nDid you find it? 👇\n" + FOLLOW + "\n\n#chess #chesspuzzle #anastasiasmate #checkmate #shorts",
  ["chess", "chess puzzle", "anastasias mate", "mate in 1", "checkmate patterns"])

# 27 Loyd stalemate
add("fastest-stalemate", {"title": "The fastest stalemate ever", "segments": [
  {"say": "Can a chess game end in a draw after just ten moves? Watch this.", "caption": "A 10-move draw?"},
  {"say": "White's queen goes hunting, eating pawn after pawn.", "moves": ["e3","a5","Qh5","Ra6","Qxa5","h5","h4","Rah6","Qxc7","f6"], "caption": "Queen goes hunting"},
  {"say": "More captures. The queen eats the bishop and knight.", "moves": ["Qxd7+","Kf7","Qxb7","Qd3","Qxb8","Qh7","Qxc8","Kg6"], "caption": "Eating everything"},
  {"say": "Queen e6. And Black has no legal moves. Stalemate after ten moves.", "moves": ["Qe6"], "caption": "Queen e6"},
  {"say": "This puzzle was composed by Sam Loyd. Black is boxed in by its own pieces. A draw!", "banner": "STALEMATE"},
  {"say": "Did you know a game could end like this? Comment below.", "caption": "Did you know this?"}]},
  "The fastest STALEMATE possible: 10 moves 🤯 #chess",
  "The shortest known stalemate, composed by Sam Loyd: 1.e3 a5 2.Qh5 Ra6 3.Qxa5 h5 4.h4 Rah6 5.Qxc7 f6 6.Qxd7+ Kf7 7.Qxb7 Qd3 8.Qxb8 Qh7 9.Qxc8 Kg6 10.Qe6 - stalemate!\n\nBlack has pieces left but none can move, and the king isn't in check.\n\nDid you know a game could end like this? 👇\n" + FOLLOW + "\n\n#chess #stalemate #samloyd #chessfacts #shorts",
  ["chess", "stalemate", "sam loyd", "chess facts", "chess records"])

if __name__ == "__main__":
    os.makedirs("batch2", exist_ok=True)
    for i, e in enumerate(S, start=9):
        e["num"] = i
        json.dump(e, open(f"batch2/{i:02d}-{e['slug']}.json", "w"), ensure_ascii=False, indent=1)
    print(len(S), "entries")
