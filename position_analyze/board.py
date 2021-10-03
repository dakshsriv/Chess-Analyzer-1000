from stockfish import Stockfish

class Board:
    def __init__(self, fen):
        self.fen = fen
        stockfish_instance = Stockfish("/home/daksh/Projects/Chess-Analyzer-1000/Engines/stockfish_14_linux_x64/stockfish_14_x64")
        stockfish_instance.set_fen_position(fen)
        self.stockfish_inst = stockfish_instance
    
    def get_eval(self):
        eval = self.stockfish_inst.get_evaluation()
        cp = eval["value"]
        topmoves = self.stockfish_inst.get_top_moves(3)
        if eval["type"] == "mate":
            print(f"Checkmate in {cp*-1} moves")
            return self.stockfish_inst, cp*10000, topmoves
        else:
            cpfromzero = cp/100
        if cp > 0:
            print(f"The situation is in white's favour by {cp/100} points")
        elif cp < 0:
            print(f"The situation is in black's favour by {cp*-1/100} points")
            cpfromzero *= -1
        if cpfromzero <= 0.1:
            print("However, this advantage is negligible.")
        elif cpfromzero < 1:
            print("However, this advantage is easy to equalize. It can be obtained from tiny gambits.")
        elif cpfromzero < 3:
            print("This type of advantage is obtained primarily from other sacrifices or gambits. If not from one, this can be tough to equalize.")
        elif cpfromzero < 9:
            print("This is a considerable advantage caused by big sacrificing or blundering. Recovering is basically hopeless.")
        elif cpfromzero < 30:
            print("This is a colossal advantage that is almost always a guaranteed win")
        else:
            print("This is a perfectly equal position.")
        loops = 0
        for x in topmoves:
            loops = loops + 1
            try:
                print(f'{loops}. {x["Move"]} yielding {(x["Centipawn"])/100}')
            except TypeError:
                print(f'{loops}. {x["Move"]} yielding {(x["Mate"])}')
        return (cp/100), topmoves


    def getStats(self):
        move = "c5f2"
        eval, bestmoves = self.get_eval()
        print(eval,bestmoves)
        moveQuality = str()
        bls, isMate = posUtils.moves_mate(bestmoves)
        (self.stockfish_inst).make_moves_from_current_position([move])
        eval2, bestmoves2 = self.get_eval()
        bls2, isMate2 = posUtils.moves_mate(bestmoves2)
        moveQuality = posUtils.move_quality(isMate, isMate2, eval, eval2, move, bls)
        return [moveQuality, eval, bls, eval2, bls2]

class posUtils:

    def moves_mate(bestmoves):
        bls = [x["Move"] for x in bestmoves]
        checkmates = [x["Mate"] for x in bestmoves]
        for x in range(0, len(checkmates)):
            if checkmates[x] == None:
                checkmates[x] = False
        isMate = checkmates[0] or checkmates[1] or checkmates[2]
        return bls, isMate
    
    def move_quality(isMate, isMate2, eval, eval2, move, bls):
        if not isMate and isMate2:
            moveQuality = "Blunder"
        if not isMate2 and isMate:
            moveQuality = "Missed Win"
        if not isMate and not isMate2:
            eDbm = -1*abs(eval2 - eval)
            if eDbm <= -3:
                moveQuality = "Blunder"
            elif eDbm <= -2:
                moveQuality = "Big Mistake"
            elif eDbm <= -1:
                moveQuality = "Small Mistake"
            elif eDbm <= 0.5:
                moveQuality = "Inaccuracy"

            if move == bls[0]:
            #print("Best move!")
                moveQuality = "Best move"
            elif move == bls[1]:
                moveQuality = "Best move"
            elif move == bls[2]:
                moveQuality = "Best move"