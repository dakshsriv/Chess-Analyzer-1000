import moveAnalyze, chess, depthString

print("Deep positiong's access GRANTED!")

def anylz(fen, move):
    print("Basic explanation of best move:")
    stockfish, eval, bls, _, _ = moveAnalyze.getStats(fen, move)
    print(f"In the current position, the best move is {bls[0]}. It: ")
    depthString1 = depthString(stockfish)
    stockfish.set_fen_position("r1bqk2r/pppp1Npp/2n2n2/2b1p3/2B1P3/8/PPPP1PPP/RNBQK2R b KQkq - 0 5")