#!/usr/bin/env python3

#import position_analyze
import math
import position_analyze.moveAnalyze
import pytest, pprint
from stockfish import Stockfish

def gb(fen, move):
    stockfish = Stockfish("Engines/stockfish_14_linux_x64/stockfish_14_x64")
    stockfish = Stockfish(parameters={"Threads": 3, "Minimum Thinking Time": 30, "Ponder": True})
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
    
def test_bestmove1():
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

def test_bestmove2():
    #fen2 = "r1b1k2r/pp3ppp/2p5/3p4/3P4/2n5/PPP3PP/R1B1KB2 w kq - 0 17"
    move = "c6d4"
    fen = "r3k2r/ppp2Npp/2n5/3Bpb2/5q2/8/PPPPK1PP/RNBQ3R b kq - 2 11"
    lz = position_analyze.moveAnalyze.getStats(fen, move)
    lz[2] = set(lz[2])
    lz[4] = set(lz[4])
    pprint.pprint(lz)
    eval, bls, eval2, bls2 = gb(fen, move)
    la = ["Best move", eval, bls, eval2, bls2]
    pprint.pprint(la)
    #assert ["Best move", eval, bls, eval2, bls2] == lz
    assert la == lz

def test_inaccuracy():
    move = "f8b4"
    fen = "r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 2 3"
    lz = position_analyze.moveAnalyze.getStats(fen, move)
    lz[2] = set(lz[2])
    lz[4] = set(lz[4])
    pprint.pprint(lz)
    eval, bls, eval2, bls2 = gb(fen, move)
    la = ["Inaccuracy", eval, bls, eval2, bls2]
    pprint.pprint(la)
    #assert ["Best move", eval, bls, eval2, bls2] == lz
    assert la == lz

#test_bestmove1()
#test_bestmove2()
