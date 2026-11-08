import json
S=lambda say,**k: dict(say=say,**k)
spec={"title":"10 Chess Openings That Win Games",
"intro":[S("Ten chess openings that actually win games. Five for White, five for Black, and each one comes with the idea or trap that wins. Stay for number eight: a checkmate in six moves that still catches people online.",
           caption="5 for White. 5 for Black. Every one with a trap or plan.", banner="10 OPENINGS")],
"chapters":[
 {"name":"Italian Game","side":"White","segments":[
   S("Number one, the Italian Game. e4, e5. Knight f3, knight c6. Bishop c4.",moves=["e4","e5","Nf3","Nc6","Bc4"],caption="The bishop aims at f7",arrows=[["c4","f7"]]),
   S("Why f7? It's the weakest square in Black's camp, because only the king defends it. Your bishop is already staring at it.",caption="f7 is only defended by the king",arrows=[["c4","f7"]]),
   S("If Black plays the natural knight f6, jump in with knight g5. Now two pieces hit f7.",moves=["Nf6","Ng5"],caption="Two attackers on f7",arrows=[["g5","f7"],["c4","f7"]]),
   S("Black's best is d5. But if Black takes back with the knight, you sacrifice on f7. This is the famous Fried Liver Attack.",moves=["d5","exd5","Nxd5","Nxf7"],caption="The Fried Liver Attack",banner="SACRIFICE!"),
   S("King takes, queen f3 check, and the black king has to walk forward into the open. White gets a huge attack against a king in the middle of the board.",moves=["Kxf7","Qf3+","Ke6","Nc3"],caption="Black's king is stuck in the center",arrows=[["c3","d5"],["f3","d5"]]),
 ]},
 {"name":"Ruy Lopez","side":"White","segments":[
   S("Number two, the Ruy Lopez, the oldest opening that world champions still play. e4, e5. Knight f3, knight c6. Bishop b5.",moves=["e4","e5","Nf3","Nc6","Bb5"],caption="Attack the defender of e5",arrows=[["b5","c6"]]),
   S("The bishop attacks the knight that protects e5. Black usually asks the question with a6.",moves=["a6"],caption="Black asks: take or retreat?"),
   S("Here's the beginner mistake. Bishop takes c6, pawn takes back, and you grab e5. Looks like a free pawn.",moves=["Bxc6","dxc6","Nxe5"],caption="A free pawn? Not so fast"),
   S("Queen d4! The queen attacks the knight and the e4 pawn at the same time, and Black wins the pawn right back.",moves=["Qd4"],caption="Fork: the knight AND e4",banner="QUEEN FORK",arrows=[["d4","e5"],["d4","e4"]]),
   S("So don't rush. The main line is bishop a4, knight f6, and castle. Slow pressure that wins long games.",reset=True,moves=["e4","e5","Nf3","Nc6","Bb5","a6","Ba4","Nf6","O-O"],caption="Main line: retreat and castle"),
 ]},
 {"name":"Scotch Game","side":"White","segments":[
   S("Number three, the Scotch. Instead of slow play, you open the center right away. e4, e5. Knight f3, knight c6. d4!",moves=["e4","e5","Nf3","Nc6","d4"],caption="Hit the center on move three",arrows=[["d4","e5"]]),
   S("Black takes, you take back with the knight, and you get a strong central knight and easy development.",moves=["exd4","Nxd4"],caption="Open lines, fast development"),
   S("A common line: bishop c5, bishop e3, queen f6, c3. Your knight on d4 is rock solid.",moves=["Bc5","Be3","Qf6","c3"],caption="c3 supports the knight",arrows=[["c3","d4"],["e3","d4"]]),
   S("Garry Kasparov and Magnus Carlsen have both played the Scotch. Simple ideas, open position, perfect if you like to attack.",caption="Played by Kasparov and Carlsen"),
 ]},
 {"name":"Queen's Gambit","side":"White","segments":[
   S("Number four, the Queen's Gambit. d4, d5, c4. You offer a pawn to take over the center.",moves=["d4","d5","c4"],caption="Offer a pawn for the center",arrows=[["c4","d5"]]),
   S("If Black grabs it, play e3. Your bishop will win the pawn back. But watch what happens if Black tries to hold on to it with b5 and c6.",moves=["dxc4","e3","b5","a4","c6","axb5","cxb5"],caption="Black tries to keep the pawn"),
   S("Queen f3! The long diagonal is wide open, and the rook on a8 is attacked. Black loses material.",moves=["Qf3"],caption="The a8 rook is attacked",banner="QUEEN F3!",arrows=[["f3","a8"]]),
   S("If Black declines with e6, just keep developing. Knight c3, knight f6, bishop g5. Easy, natural moves.",reset=True,moves=["d4","d5","c4","e6","Nc3","Nf6","Bg5"],caption="Declined: just develop"),
 ]},
 {"name":"London System","side":"White","segments":[
   S("Number five, the London System, for players who hate memorizing. d4, then bishop f4, and you play the same setup against almost everything.",moves=["d4","d5","Bf4"],caption="Bishop out BEFORE e3"),
   S("e3, knight f3, bishop d3, knight d2, c3. A solid pawn pyramid, and every piece has a home.",moves=["Nf6","e3","e6","Nf3","Bd6","Bd3","O-O","Nbd2","c5","c3"],caption="The same setup every game"),
   S("Just watch for one thing. When Black plays c5 and queen b6, your b2 pawn is attacked. Defend it with queen c1 or queen b3.",reset=True,moves=["d4","d5","Bf4","c5","e3","Qb6"],caption="Watch your b2 pawn",arrows=[["b6","b2"]]),
 ]},
 {"name":"Sicilian Defense","side":"Black","flip":True,"segments":[
   S("Now the openings for Black. Number six: against e4, the Sicilian, c5. The most popular and most fighting answer.",moves=["e4","c5"],caption="Fight for d4 from the side",arrows=[["c5","d4"]]),
   S("Black controls d4 from the side and keeps the center pawns for later. The position is unbalanced from move one, so Black plays to win, not to draw.",caption="Unbalanced = chances to win"),
   S("The main line: knight f3, d6, d4, pawn takes, knight takes, knight f6, knight c3, a6. That's the Najdorf, the favorite of Fischer and Kasparov.",moves=["Nf3","d6","d4","cxd4","Nxd4","Nf6","Nc3","a6"],caption="The Najdorf: Fischer and Kasparov"),
   S("Notice the trade: Black gave a side pawn for White's center pawn. That extra central pawn is a big reason the Sicilian scores so well.",caption="Side pawn for a center pawn"),
 ]},
 {"name":"French Defense","side":"Black","flip":True,"segments":[
   S("Number seven, the French Defense. e4, e6. d4, d5. Black builds a wall and challenges the center right away.",moves=["e4","e6","d4","d5"],caption="Build a wall, hit e4",arrows=[["d5","e4"]]),
   S("If White pushes e5, attack the chain at its base. c5, then knight c6 and queen b6. Everything hits d4.",moves=["e5","c5","c3","Nc6","Nf3","Qb6"],caption="Attack the base: d4",arrows=[["c5","d4"],["b6","d4"],["c6","d4"]]),
   S("One downside: the bishop on c8 is stuck behind the e6 pawn. Plan to trade it or free it later.",caption="Watch the c8 bishop"),
 ]},
 {"name":"Caro-Kann Defense","side":"Black","flip":True,"segments":[
   S("Number eight, the Caro-Kann. e4, c6. d4, d5. Solid like the French, but the c8 bishop stays free.",moves=["e4","c6","d4","d5"],caption="Solid, and the bishop stays free"),
   S("Classical line: knight c3, pawn takes, knight takes, bishop f5. The bishop gets out before e6.",moves=["Nc3","dxe4","Nxe4","Bf5"],caption="Bishop out before e6",arrows=[["f5","e4"]]),
   S("Now the trap you must know. Instead of bishop f5, Black plays knight d7. White plays queen e2. And Black plays the natural knight f6...",reset=True,moves=["e4","c6","d4","d5","Nc3","dxe4","Nxe4","Nd7","Qe2","Ngf6"],caption="Looks natural. It loses."),
   S("Knight d6. Checkmate! The e7 pawn is pinned by the queen, so it can't take. Smothered mate in six moves.",moves=["Nd6#"],expect_mate=True,caption="The e7 pawn is pinned"),
 ]},
 {"name":"King's Indian Defense","side":"Black","flip":True,"segments":[
   S("Number nine, against d4: the King's Indian. Knight f6, g6, bishop g7, d6, castle. Black lets White take the center, then attacks it.",moves=["d4","Nf6","c4","g6","Nc3","Bg7","e4","d6","Nf3","O-O"],caption="Let White take the center..."),
   S("Then Black strikes with e5. When White closes the center with d5, the knight goes to e7.",moves=["Be2","e5","O-O","Nc6","d5","Ne7"],caption="...then strike with e5"),
   S("And now the f-pawn charges with f5, straight at the white king. This is how Bobby Fischer and Garry Kasparov won game after game.",caption="Next: f5 and attack the king",arrows=[["f7","f5"]]),
 ]},
 {"name":"Scandinavian Defense","side":"Black","flip":True,"segments":[
   S("Number ten, the Scandinavian. e4, d5. Black challenges e4 on move one.",moves=["e4","d5"],caption="Challenge e4 immediately",arrows=[["d5","e4"]]),
   S("Pawn takes, queen takes back. The queen comes out early, but after knight c3 it goes to a5, safe and out of the way.",moves=["exd5","Qxd5","Nc3","Qa5"],caption="Queen to a5: safe"),
   S("Then knight f6, c6, bishop f5. An easy setup you can learn in ten minutes, and it works against almost every e4 player.",moves=["d4","Nf6","Nf3","c6","Bc4","Bf5"],caption="Easy setup, learn it fast"),
 ]},
],
"outro":[S("So which one are you playing in your next game? Tell me in the comments, and subscribe for daily chess traps and puzzles.",caption="Which one will you play? Comment below!",banner="SUBSCRIBE")]}
json.dump(spec,open("long/long1.json","w"),indent=1)
