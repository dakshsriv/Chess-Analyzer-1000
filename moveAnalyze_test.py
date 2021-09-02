#!/usr/bin/env python3

#import position_analyze
import math
import position_analyze.moveAnalyze
import pytest, pprint
from stockfish import Stockfish

def gb(fen, move):
    stockfish = Stockfish("Engines/stockfish_14_linux_x64/stockfish_14_x64")
    stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 30, "Ponder": True})
    stockfish.set_fen_position(fen)
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

    return eval, bls, eval2, bls2
    
def test_bestmove():
    move = "c5f2"
    fen = "r1bqk2r/pppp1Npp/2n2n2/2b1p3/2B1P3/8/PPPP1PPP/RNBQK2R b KQkq - 0 5"
    lz = position_analyze.moveAnalyze.getStats(fen, move)
    lz[2] = set(lz[2])
    lz[4] = set(lz[4])
    pprint.pprint(lz)
    eval, bls, eval2, bls2 = gb(fen, move)
    la = ["Best move", eval, bls, eval2, bls2]
    pprint.pprint(la)
    #assert ["Best move", eval, bls, eval2, bls2] == lz
    assert la == lz
    #fen2 = "r1b1k2r/pp3ppp/2p5/3p4/3P4/2n5/PPP3PP/R1B1KB2 w kq - 0 17"
    move2 = "b2b3"
    fen2 = "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
    lz2 = position_analyze.moveAnalyze.getStats(fen2, move2)
    lz2[2] = set(lz2[2])
    lz2[4] = set(lz2[4])
    pprint.pprint(lz2)
    eval2, bls2, eval22, bls22 = gb(fen2, move2)
    la2 = ["Best move", eval2, bls2, eval22, bls22]
    pprint.pprint(la2)
    assert la2 != lz2


test_bestmove()
