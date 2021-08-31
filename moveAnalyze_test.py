#!/usr/bin/env python3

#import position_analyze
import math
import position_analyze.moveAnalyze
import pytest, pprint
from stockfish import Stockfish

def test_bestmove1():
    move = "b8c6"
    fen = "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
    stockfish = Stockfish("Engines/stockfish_14_linux_x64/stockfish_14_x64")
    stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 30, "Ponder": True})
    stockfish.set_fen_position(fen)
    global eval
    eval = stockfish.get_evaluation()
    cp = eval["value"]
    print(eval)
    if eval["type"] == "mate":
        eval = cp*10000
    else:
        eval = cp/100
    bls = stockfish.get_top_moves(3)
    bls = [x["Move"] for x in bls]
    stockfish.make_moves_from_current_position([move])
    eval2 = stockfish.get_evaluation()
    cp2 = eval2["value"]
    if eval2["type"] == "mate":
        eval2 = cp2*10000
    else:
        eval2 = cp2/100
    bls2 = stockfish.get_top_moves(3)
    bls2 = [x["Move"] for x in bls2]
    bls = set(bls)
    bls2 = set(bls2)
    lz = position_analyze.moveAnalyze.getStats(fen, move)
    lz[2] = set(lz[2])
    lz[4] = set(lz[4])
    pprint.pprint(lz)
    la = ["Best move", eval, bls, eval2, bls2]
    pprint.pprint(la)
    #assert ["Best move", eval, bls, eval2, bls2] == lz
    assert la == lz 


test_bestmove1()
