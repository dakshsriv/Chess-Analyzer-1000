import moveAnalyze, chess

print("Deep positiong's access GRANTED!")

def anylz(fen, move):
    print("Basic explanation of best move:")
    stockfish, eval, bls, _, _ = moveAnalyze.getStats(fen, move)
    print(f"In the current position, the best move is {bls[0]}. It: ")
