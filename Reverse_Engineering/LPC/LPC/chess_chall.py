#!/usr/bin/python
import chess
import chess.engine
import random
import time
arr = [
"3rr3/8/2p3Pk/1p2nP1p/pP2p1P1/P1B1Nb1B/2P2K2/6R1 b - - 2 40 ",
"r4r1k/4bpp1/p2p1nbp/2p2P2/2PnP3/2NP4/R2B1N1P/3B1RK1 b - - 0 26 ",
"3rr1k1/1p1n4/1qp4p/4ppbb/pP2P3/P3NPP1/1BP1R1B1/R1Q4K w - f6 0 29   ",
"r4r1k/4bpp1/p2p1nbp/q1p5/2PnPPB1/P1NP4/1R1B1N1P/3Q1RK1 b - - 2 23  ",
"1k1r4/pp3pp1/1n1q4/2p3Pp/6n1/2P2NP1/PPQ2PB1/1K2R3 w - - 7 29   ",
"2k1rr2/pp3qp1/2p1n1p1/1PnpP3/6PP/P1NQ1NR1/2P2P2/1K2R3 w - - 1 27   ",
"3rr1k1/1p1n4/1qp4p/4pPbb/pP6/P3NPP1/1BP1R1B1/R1Q4K b - - 0 29  ",
"3rr1k1/1p6/2p3P1/4nP1p/pP2p3/P1B1NbP1/2P3B1/5RK1 b - - 1 36    ",
"1r6/2r2p1k/5Pbp/RBp1p3/2P1P1K1/3P4/8/5R2 b - - 0 42    ",
"r2qrbk1/3b1ppn/p2p3p/1ppPp3/P3P3/1PP1B1NP/2B1QPP1/R3R1K1 w - - 2 22    ",
"3rr1k1/1p1n1p2/1qp2n1p/p1b1p1pb/4P3/PP2N1PP/1BP2PB1/R1Q1RNK1 b - - 4 22    ",
"r4r1k/4bpp1/p2p1nbp/2p5/2PnPPB1/q1NP4/1R1B1N1P/3Q1RK1 w - - 0 24   ",
"r1r1q1k1/6p1/3b1p1p/1p1PpP2/1Pp1B3/2P4P/R4QP1/R5K1 b - - 1 37  ",
"r2qk2r/pp3pp1/2p1pn2/4n2p/1b6/3P2PP/PPPNQPB1/R1B1K2R b KQkq - 1 12 ",
"rn1qkb1r/pp2pppp/2pp1n2/7b/3PP3/2NB1N1P/PPP2PP1/R1BQK2R b KQkq - 2 6   ",
"rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2 ",
"5r2/p1k3p1/2p3R1/3pP3/2r4P/P6R/2P5/K7 b - - 0 40   ",
"3rr1k1/1p1n1p2/1qp4p/4p1bb/pP2P3/P3NPP1/1BP1R1B1/R1Q4K b - - 0 28  ",
"r2qkb1r/pp1n1ppp/2p1pn2/3p4/6b1/1P1P1NP1/PBP1PPBP/RN1Q1RK1 b kq - 0 7  ",
"r2qkbnr/pp1n1ppp/2p1p3/3p4/8/3P1BPP/PPP1PP2/RNBQK2R w KQkq - 0 7   ",
"3r3k/2r2p2/R4Pbp/1Bp1p3/2P1P2K/3P1R2/8/8 b - - 8 46    ",
"3rr1k1/1p1n1p2/1qp4p/p1b1p2b/4P3/PP2NPP1/1BP3B1/R1Q1R1K1 b - - 0 25    ",
"2k1rr2/p5p1/2p1n1p1/2npP3/5qPP/P1N1QNR1/2P2P2/1K2R3 w - - 0 29 ",
"r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 5    ",
"rn2k2r/pp1nqppp/2p1p3/3pP2b/3P4/2NB1N1P/PPP1QPP1/R3K2R w KQkq - 0 11   ",
"2n5/ppkr2p1/6R1/2pB2Pp/2P4N/1P4P1/P4n2/1K6 b - - 4 35  ",
"1k1r4/ppq2pp1/1n6/2p3Pp/Q5n1/2P2NP1/PP3PB1/1K2R3 w - - 5 28    ",
"2k1rr2/pp1n2p1/2p1n1p1/3pP3/5qPP/P4NR1/1PP1QP2/1K1NR3 w - - 1 23   ",
"r4r1k/4bppb/p2p1n1p/2p2P2/2PnP3/2NP3N/R2B3P/3B1RK1 b - - 2 27  ",
"r1bq1rk1/2p1bppp/p1np1n2/1p2p3/4P3/1BP2N2/PP1P1PPP/RNBQR1K1 w - - 1 9  ",
"r2qk2r/pp3pp1/2p1pn2/4n2p/1b6/3P2PP/PPPN1PB1/R1BQK2R w KQkq h6 0 12    ",
"8/ppk3p1/4R3/1Ppr2Pp/7N/1P4P1/P4n2/1K6 w - - 0 38  ",
"5r2/p5R1/1kp5/3pP3/7P/PR6/2r5/K7 b - - 2 42    ",
"2k1rr2/ppnn2p1/2p2qp1/3pP3/6PP/5NR1/PPP1QP2/1K1NR3 b - - 0 21  ",
"rnbnkqrb/pppppppp/8/8/8/8/PPPPPPPP/RNBNKQRB w KQkq - 0 1   ",
"r3k2r/ppq2pp1/2p1pn2/4n2p/1b6/3P2PP/PPPNQPB1/R1B1K2R w KQkq - 2 13 ",
"rr5k/4bppb/p2p1n1p/2p2P2/2PnPN2/2NP4/R2B3P/3B1RK1 b - - 4 28   ",
"r2qrbk1/3b1pp1/p1np1n1p/1ppPp3/4P3/1PP2NNP/P1B2PP1/R1BQR1K1 b - - 0 16 ",
"2k1rr2/ppnn2p1/2p3p1/3pP3/5qPP/P4NR1/1PP1QP2/1K1NR3 b - - 0 22 ",
"r2qkbnr/pp1npppp/2p5/3p4/8/3P1BPP/PPP1PP2/RNBQK2R b KQkq - 0 6 ",
"5r2/p1k3p1/2p3p1/3pP3/3r3P/P6R/2P5/KR6 w - - 0 39  ",
"r4r1k/2q1bpp1/p2p1nbp/2p1p3/2PnP1B1/P1NPBPP1/1R3N1P/3Q1RK1 w - - 4 21  ",
"1r6/r1b2p1k/5Pbp/pBpNp3/2P1P1K1/3P4/R7/5R2 w - - 3 41  ",
"8/R7/2p5/2kpP3/7P/P7/2r5/KR3r2 b - - 2 44  ",
"r1r1qbk1/3b1pp1/p2n3p/1pBPpN2/PPp1P3/2P4P/R1B2QP1/R5K1 b - - 11 33 ",
"r2q1rk1/pp1n1pp1/2pbpn1p/3p3b/8/1P1PPNPP/PBPN1PB1/R2Q1RK1 w - - 0 11   ",
"r4rk1/ppbn1p2/2p2n1p/q2pp1pb/4P3/PP1P1NPP/1BPN1PB1/R3QRK1 b - - 0 15   ",
"r1bqrbk1/2p2pp1/p1np1n1p/1p2p3/3PP3/1BP2N1P/PP3PP1/R1BQRNK1 b - - 4 12 ",
"rn1qkbnr/ppp1pppp/8/3p4/6b1/1P3NP1/P1PPPP1P/RNBQKB1R b KQkq - 0 3  ",
"r4rk1/pppqbppp/2np1n2/4p1N1/2P1P1b1/P1NP2P1/1P3PBP/R1BQ1RK1 w - - 1 11 ",
"5r2/p1k2rp1/2p1n1p1/2npP3/3N2PP/P1N1P2R/2P5/K2R4 b - - 4 33    ",
"8/ppk5/4R3/1Pp3P1/5N2/1n4P1/3r4/1K6 b - - 3 46 ",
"3rr1k1/1p6/2p3Pp/4nP2/pP2p3/P1B1NbP1/2P3B1/5R1K b - - 0 35 ",
"1k1r4/ppq2pp1/1n6/2p3Pp/6n1/2P2NP1/PPQ2PB1/1K2R3 b - - 6 28    ",
"8/2R1P3/8/2pp4/2k1r3/P7/8/1K6 w - - 1 55   ",
"rnbqkb1r/pp2pppp/2pp1n2/8/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 2 4   ",
"3rr1k1/1p1n4/1qp4p/5PP1/pP2p3/P3N1P1/1BP1b1B1/R1Q4K b - - 0 31 ",
"8/ppk5/8/1P4P1/2p2N2/1n2R1P1/3r4/1K6 b - - 1 47    ",
"3rr1k1/1p1n1p2/1qp2n1p/p1b1p2b/4P1P1/PP2N1P1/1BP2PB1/R1Q1RNK1 b - - 0 23   ",
"2krr3/ppq1bpp1/2p3n1/6Bp/3N2nP/2P3P1/PPQ2PB1/2KR3R b - - 6 20  ",
"3rr3/6k1/2p3P1/1p2nP1p/pP2p3/P1B1NbPB/2P2K2/5R2 w - - 2 39 ",
"2kr3r/pp1nqpp1/n1p1p1p1/3pP3/3P2PP/2N2N2/PPP1QP2/2K3RR b - - 4 15  ",
"2r3k1/Q2q2p1/3b1p1p/1p1PpP2/1Pp1B3/2P4P/6P1/R5K1 b - - 2 39    ",
"r1b1kb1r/pp1nq1p1/2p1pn1p/8/3P4/3B1N2/PPP2PPP/R1BQ1RK1 w kq - 0 10 ",
"r2qkb1r/pp1n1ppp/2p1pn2/3p4/6b1/1P3NP1/PBPPPPBP/RN1Q1RK1 w kq - 0 7    ",
"r4r1k/p2qbpp1/1p1p1n1p/2p1p2b/1PPnP3/P1NPBPP1/1R3NBP/3Q1RK1 b - - 3 17 ",
"2r1q1k1/6p1/3b1p1p/1p1PpP2/1Pp1B3/2P4P/r4QP1/R5K1 w - - 0 38   ",
"r1b1kb1r/pp1nq1p1/2p1pnBp/8/3P4/5N2/PPP2PPP/R1BQ1RK1 b kq - 1 10   ",
"rr1b3k/5ppb/p2p1n1p/2pNnP2/B1P1PB2/2NP4/R6P/5RK1 b - - 10 31   ",
"3rr1k1/1p1nbp2/1qp4p/p3p2b/4P3/PP2NPP1/1BP3B1/R1Q1R1K1 w - - 1 26  ",
"2kr3r/ppnn2p1/2p1pqp1/3p4/3P2PP/2N2N2/PPP1QP2/1K4RR w - - 0 18 ",
"rnbqkbnr/pp1ppppp/2p5/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq d3 0 2  ",
"2k1r2r/ppnn2p1/2p1pqp1/3p4/3P2PP/2N2NR1/PPP1QP2/1K2R3 b - - 3 19   ",
"rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1 ",
"rn1qkb1r/pp3ppp/2p1pn2/3p2Bb/3PP3/2NB1N1P/PPP1QPP1/R3K2R b KQkq - 1 8  ",
"1k2r3/ppq2pp1/8/2p3Pp/Q1n3n1/2P2NP1/PP3PB1/1K1R4 b - - 2 26    ",
"8/ppkr2p1/6R1/1Pp3Pp/7N/1P4P1/P4n2/1K6 w - - 2 39  ",
"r3k2r/ppq1bpp1/2p2nn1/7p/3N3P/2P3P1/PP2QPB1/R1B1K2R b KQkq - 0 17  ",
"8/2R5/8/2ppP3/2k4P/P7/7r/1K6 w - - 0 53    ",
"r1k2b1r/pb1nq1p1/2p1p1Bp/1p1n4/P2P4/5NB1/1PP2PPP/R2QR1K1 w - - 5 15    ",
"r1rq1bk1/3b1pp1/p2n3p/1p1Pp3/PPp1P3/R1P1B1NP/2B2QP1/R5K1 w - - 4 30    ",
"r1bqrbk1/2p2pp1/p1np1n1p/1p2p3/3PP3/1BP2N1P/PP1N1PP1/R1BQR1K1 w - - 3 12   ",
"r2qrbk1/3b1pp1/p2p1nnp/1ppPp3/4P3/1PP1BNNP/P1B2PP1/R2QR1K1 w - - 3 18  ",
"r1rq1bk1/3b1pp1/p2p1n1p/1p1PP3/PPp1P3/R1P1B1NP/2B1Q1P1/R5K1 b - - 0 27 ",
"5r2/p1k3p1/2p1n1p1/2npP3/3N2rP/P3P2R/2P1N3/KR6 w - - 0 36  ",
"8/2R5/2p5/3pP3/2k4P/P7/7r/1K6 b - - 6 52   ",
"r3rbk1/3b1ppn/p2p3p/1ppPp3/P3P2q/1PP1B1NP/2B1QPP1/R3R1K1 b - - 1 21    ",
"r1bqk2r/2ppbppp/p1n2n2/1p2p3/4P3/1B3N2/PPPP1PPP/RNBQR1K1 b kq - 1 7    ",
"r4rk1/ppbn1pp1/2p1pn1p/q2p3b/7N/PP1PP1PP/1BPN1PB1/R3QRK1 b - - 2 13    ",
"rn1qkbnr/ppp1pppp/8/3p4/6b1/5NP1/PPPPPP1P/RNBQKB1R w KQkq - 1 3    ",
"4r3/p1k2rp1/2p1n1p1/2npP3/6PP/P1N1PNR1/2P5/K2R4 w - - 1 32 ",
"8/4R3/2p5/2kpP3/7P/P7/4r3/1K6 b - - 2 50   ",
"r3r1k1/1p1n1p2/1qpb1n1p/p2pp1pb/4P3/PP1P2PP/1BP2PBN/R1Q1RNK1 b - - 3 19    ",
"4rr2/p1k3p1/2p1n1p1/2npP3/5qPP/P1N1QNR1/2P2P2/K2R4 b - - 3 30  ",
"r3r1k1/1p1n1p2/1qpb1n1p/p2pp1pb/4P3/PP1P2PP/1BPN1PBN/R1Q1R1K1 w - - 2 19   ",
"3rr3/8/2p3Pk/1p2nP2/pP2p1N1/P1B5/2P2K2/6R1 b - - 0 42  ",
"8/R7/2p5/2kpP3/7P/P7/5r2/KRr5 b - - 10 48  ",
"R7/1rq2kp1/2Qb1p1p/1p1PpP2/1Pp1B3/2P4P/6P1/6K1 b - - 10 43 ",
"R7/1r1q1kp1/Q2b1p1p/1p1PpP2/1Pp1B3/2P4P/6P1/6K1 b - - 8 42 ",
"1k1r4/pp4p1/1n4p1/2p3Pp/2P5/1P3NP1/P4nB1/1K2R3 w - - 0 32  "
]

toxic_msges = [
    "so bad lmfaoo",
    "git gud",
    "sooooo ez u noob",
    "are you paying attention?",
    "fight me noob",
    "mad cuz bad",
    "You are just trash",
    "iq = elo = 0",
    "i bet your main category is steg",
    "try alt+f4 to win",
    "this aint checkers man",
    "L nerd",
    "Tu mere level da banda e nhi aa shoreya",
    "Your gameplay is a prime example of what not to do in chess.",
    "Your moves are as effective as a chocolate teapot.",
    "Your strategy is like a flat tire - going nowhere fast.",
    "If brains were dynamite, you wouldn't have enough to blow your nose.",
    "You're not just losing, you're donating wins to the opponent.",
    "Even amateur players are cringing at your gameplay.",
    "You're like a walking advertisement for chess disasters.",
    "Your moves are so bad, even the chess clock is laughing at you.",
    "Your gameplay is a textbook example of strategic mismanagement.",
    "You're not just playing chess, you're performing a symphony of failure."

]

slangs_uwu = [
    "Your moves are so bad, they should be classified as a humanitarian crisis.",
"You're not just losing, you're rewriting the definition of failure.",
"If failure was an art, you'd be Picasso.",
"I've seen better strategies from a toddler playing with blocks.",
"Your moves are like a broken record - repetitive and annoying.",
"Are you playing chess or just randomly moving pieces around?",
"Even a blindfolded player could beat you with one hand tied behind their back.",
"Your gameplay is the reason why we have warning labels.",
"You're not just losing, you're single-handedly keeping the opponents entertained.",
"Congratulations, you're the reigning champion of disappointment.",
"Is this a chess match or a comedy show? Because your moves are hilarious.",
"You're like a walking advertisement for anti-strategy.",
"Even the chess pieces are begging for retirement from your gameplay.",
"Your strategy is like a maze – confusing and leading nowhere.",
"Your moves are so bad, they make beginner players look like grandmasters.",
"Is this a chess game or a tutorial on how not to play?",
"You're not just losing, you're setting new records for strategic failure.",
"Your tactics are so weak, even the chessboard feels sorry for you.",
"I've seen more excitement in a game of tic-tac-toe.",
"You're not just making moves, you're making history... as the worst player ever."

]

def generate_fen_position():
    while True:
        fen = input("Enter your best move data: ").strip()
        try:
            if chess.Board(fen).is_valid():
                return fen
            else:
                print("Invalid FEN position! Please enter a valid FEN position.")
        except ValueError:
            print("Invalid move format! Please enter a move in fen")
            return "LOSER"

def print_board(fen):
    board = chess.Board(fen)
    print(board)

def generate_random_fen_position():
    board = chess.Board(random.choice(arr))
    return board.fen()

def is_best_move(fen, player_move_fen, engine):
    board = chess.Board(fen)
    best_move_uci = engine.analyse(board, chess.engine.Limit(time=0.1))['pv'][0]
    board.push(best_move_uci)
    return player_move_fen == board.fen()

def split_string_into_equal_parts(s):
    n = len(s)
    part_length = n // 5
    remainder = n % 5
    parts = []
    start = 0
    
    for i in range(5):
        end = start + part_length
        if i < remainder:
            end += 1  
        parts.append(s[start:end])
        start = end
    
    return parts

def main():
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish")
    engine.configure({"Skill Level": 20})

    print("\n\n ██▀███   ▒█████   ▒█████  ▄▄▄█████▓▒██   ██▒ ██▀███   ▄▄▄       ███▄    █ ");
    print("▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓  ██▒ ▓▒▒▒ █ █ ▒░▓██ ▒ ██▒▒████▄     ██ ▀█   █ ");
    print("▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▒ ▓██░ ▒░░░  █   ░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒");
    print("▒██▀▀█▄  ▒██   ██░▒██   ██░░ ▓██▓ ░  ░ █ █ ▒ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒");
    print("░██▓ ▒██▒░ ████▓▒░░ ████▓▒░  ▒██▒ ░ ▒██▒ ▒██▒░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░");
    print("░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░   ▒ ░░   ▒▒ ░ ░▓ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ");
    print("  ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░     ░    ░░   ░▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░");
    print("  ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░       ░    ░    ░░   ░   ░   ▒      ░   ░ ░ ");
    print("   ░         ░ ░      ░ ░            ░    ░     ░           ░  ░         ░ ");
    print("                                                                           ");
    print("Welcome to the Rootxran Chess Challenge!")
    print("You have 2 seconds to make each move.\n")
    print("You'll be always playing as black cuz ..............\n")

    correct_moves = 0

    while correct_moves < 5:
        fen = generate_random_fen_position()
        print("Current Board:")
        print_board(fen)
        print("Additional Data: " , fen.split(" ", 1)[1])
        start_time = time.time()
        player_move_san = generate_fen_position()
        elapsed_time = time.time() - start_time
        if player_move_san == "LOSER":
            
            break
        elif elapsed_time > 2:
            print("Time's up! You took too long to make your move.")
            break

        if is_best_move(fen, player_move_san, engine):
            correct_moves += 1
            print("Correct move!")
        else:
            print("Incorrect move. Try again.")
            break
        
        if correct_moves % 2 == 0:
            print("You have made", correct_moves, "correct moves.")
            print("Current Board:")
            print("Hahaha lol")
            print(random.choice(slangs_uwu))
    

    if correct_moves >= 5:
        print("You rocked it")
        flag = open('/flag.txt').read()
        flag2 = split_string_into_equal_parts(flag)
        print("Which Part of flag you want: 1-6: ")
        try:
            wow = int(input("Enter 1-5: "))
            print(flag2[wow - 1])
        except ValueError:
            print("No flag for you bad boy")
    else:
        print("\nGame over! You made", correct_moves, "correct moves.")
        print(random.choice(toxic_msges))
    engine.quit()

if __name__ == "__main__":
    main()