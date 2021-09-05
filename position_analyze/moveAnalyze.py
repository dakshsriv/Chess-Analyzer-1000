from stockfish import Stockfish
import sys

#stockfish.set_fen_position("rnbqkbnr/pppp1ppp/8/4p3/5P2/8/PPPPP1PP/RNBQKBNR w KQkq - 0 1")
#stockfish.set_fen_position("r1bqkbnr/pppp1ppp/2n5/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 3 3")
#stockfish.set_fen_position("r1bBk2r/ppp2ppp/2p5/8/4n3/3P4/PPP1KbPP/RN1Q1B1R b kq - 1 8")

#move = "g2g4"
#move = "g8f6"
move =  "bh3"

print("Access!")

def gof(stockfish):
#    print("Here is the position on the board:")
#    print()
#    print(stockfish.get_board_visual())
#    print(stockfish.get_fen_position())
#    print("  a   b   c   d   e   f   g   h")
#    print()
#    print(f"The best move is {best_move}")
    eval = stockfish.get_evaluation()
    cp = eval["value"]
#    print(eval)
    topmoves = stockfish.get_top_moves(3)
    if eval["type"] == "mate":
        print(f"Checkmate in {cp*-1} moves")
        return stockfish, cp*10000, topmoves
    else:
       cpfromzero = cp/100
#       if cp > 0:
#           print(f"The situation is in white's favour by {cp/100} points")
#       elif cp < 0:
#           print(f"The situation is in black's favour by {cp*-1/100} points")
#           cpfromzero *= -1
#       if cpfromzero <= 0.1:
#           print("However, this advantage is negligible.")
#       elif cpfromzero < 1:
#           print("However, this advantage is easy to equalize. It can be obtained from tiny gambits.")
#       elif cpfromzero < 3:
#           print("This type of advantage is obtained primarily from other sacrifices or gambits. If not from one, this can be tough to equalize.")
#       elif cpfromzero < 9:
#           print("This is a considerable advantage caused by big sacrificing or blundering. Recovering is basically hopeless.")
#       elif cpfromzero < 30:
#           print("This is a colossal advantage that is almost always a guaranteed win")
#       else:
#           print("This is a perfectly equal position.")
        #print(topmoves)
#       loops = 0
#       for x in topmoves:
#           loops = loops + 1
#           try:
#               print(f'{loops}. {x["Move"]} yielding {(x["Centipawn"])/100}')
#           except TypeError:
#               print(f'{loops}. {x["Move"]} yielding {(x["Mate"])}')
    return stockfish, (cp/100), topmoves


def getStats(fen, move):
    stockfish = Stockfish("/home/daksh/Projects/Chess_Analyzer/Engines/stockfish_14_linux_x64/stockfish_14_x64")
    stockfish = Stockfish(parameters={"Threads": 3, "Minimum Thinking Time": 30, "Ponder": True})
    stockfish.set_fen_position(fen)
    stockfish, eval, bestmoves = gof(stockfish)
    moveQuality = str()
    bls = [x["Move"] for x in bestmoves]
    checkmates = [x["Mate"] for x in bestmoves]
    for x in range(0, len(checkmates)):
        if checkmates[x] == None:
            checkmates[x] = False
    isMate = checkmates[0] or checkmates[1] or checkmates[2]
    stockfish.make_moves_from_current_position([move])
    stockfish, eval2, bestmoves2 = gof(stockfish)
    bls2 = [x["Move"] for x in bestmoves2]
    isMate2 = False
    if eval2 <= -10000 or eval2 >= 10000:
        isMate2 = True
    if not isMate and isMate2:
        #print("Game-losing blunder! This move blunders forced mate or mate-in-one.")
        moveQuality = "Blunder"
    if not isMate2 and isMate:
        #print("Missed Win! You missed a move that could've won the game.")
        moveQuality = "Missed Win"
    print(f"eval is :{eval}, eval2 is: {eval2}")
    if not isMate and not isMate2:
        eDbm = -1*abs(eval2 - eval)
        if eDbm <= -3:
            #print("That move was a blunder! It was a very bad move.")
            moveQuality = "Blunder"
        elif eDbm <= -2:
            #print("That move was a big mistake. It was a fairly bad move.")
            moveQuality = "Big Mistake"
        elif eDbm <= -1:
            print("That move was a small mistake. It was a mildly bad move.")
            moveQuality = "Small Mistake"
        elif eDbm <= 0.5:
            moveQuality = "Inaccuracy"

        if move == bls[0]:
        #print("Best move!")
            moveQuality = "Best move"
        elif move == bls[1]:
            #print(f"Best move! {bls[0]} is an alternative.")
            moveQuality = "Best move"
        elif move == bls[2]:
            #print(f"Best move! {bls[0]} and {bls[1]} are alternatives.")
            moveQuality = "Best move"
        return [moveQuality, eval, bls, eval2, bls2]
try:
    if __name__ == "__main__" and sys.argv[1] == "-d":
        stockfish = Stockfish("Engines/stockfish_14_linux_x64/stockfish_14_x64")
        stockfish = Stockfish(parameters={"Threads": 3, "Minimum Thinking Time": 30, "Ponder": True})
        fen = sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " " + sys.argv[6] + " " + sys.argv[7]
        stockfish.set_fen_position(fen)
        move = sys.argv[8]
        print(getStats(fen, move))
except:
    pass
