from stockfish import Stockfish

stockfish = Stockfish("/home/daksh/Projects/Chess-Analyzer-1000/Engines/stockfish_14_linux_x64/stockfish_14_x64")
stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
print("Here is the position on the board:")
print()
print(stockfish.get_board_visual())
print("  a   b   c   d   e   f   g   h")
best_move = stockfish.get_best_move()
print()
print(f"The best move is {best_move}")
cp = stockfish.get_evaluation()["value"]
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
    print("This is a perfectly equal position")
