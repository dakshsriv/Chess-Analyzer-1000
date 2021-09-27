import stockfish, chess, pprint

def depthString(engine):
    depth_string = list()
    lineSums = list()
    for i in range(0, 10):
        move = engine.get_best_move()
        depth_string.append(move)
        engine.make_moves_from_current_position([move])
        topmoves = engine.get_top_moves(5)
        lineSum = 0
        for x in range(0, 3):
            lz = (topmoves[x]["Centipawn"])*(2**(-1*x))*0.01
            print("move is {} lz is {}".format(move, lz))
            lineSum = lineSum + (topmoves[x]["Centipawn"])*(2**(-1*x))*0.01
        lineSums.append(lineSum)
    return depth_string, lineSums

stockfish_instance = stockfish.Stockfish("Engines/stockfish_14_linux_x64/stockfish_14_x64")
stockfish_instance = stockfish.Stockfish(parameters={"Threads": 3, "Minimum Thinking Time": 100, "Ponder": True})
stockfish_instance.set_fen_position("r1bqk2r/pppp1Npp/2n2n2/2b1p3/2B1P3/8/PPPP1PPP/RNBQK2R b KQkq - 0 5")
pprint.pprint(depthString(stockfish_instance))