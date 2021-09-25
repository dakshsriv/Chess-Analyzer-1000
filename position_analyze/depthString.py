import stockfish, chess

def depthString(engine):
    depth_string = list()
    lineSums = list()
    for i in range(0, 10):
        move = engine.get_best_move()
        depth_string.append(move)
        engine.make_moves_from_current_position([move])
        topmoves = engine.get_top_moves(5)
        lineSum = 0
        for x in range(0, 5):
            lineSum = lineSum + (topmoves[x]["Centipawn"])*(2**(-1*x))
            print(f"LineSum is : {lineSum} {topmoves[x]["Centipawn"]} ")
        lineSums.append(lineSum)
    return depth_string, lineSums

stockfish_instance = stockfish.Stockfish("Engines/stockfish_14_linux_x64/stockfish_14_x64")
print(depthString(stockfish_instance))