#!/usr/bin/env python3

from src.Board import *
from enum import Enum

paternsAlly = ["01111", "10111", "11011", "11101", "11110"]
paternsEnemy = ["02222", "20222", "22022", "22202", "22220"]
paterns = paternsAlly + paternsEnemy

MATCHING = Enum('Matching', ['RIGHT', 'LEFT', 'DIAG_RIGHT', 'DIAG_LEFT', 'DOWN', 'NONE'])

def match_right(board, patern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for cnt in range(len(patern)): 
        if ((cnt + y) < size):
            if (gameBoard[x][y + cnt] != patern[cnt]):
                print(gameBoard[x][y + cnt], end="", flush =True)
                print(patern[cnt], end="", flush =True)
                print(" = False!", flush=True)
                return (False)
        else:
            return (False)
    return (True)

def match_left(board, patern, x, y):
    size = board.getSizeBoard()
    for cnt in range(len(patern)):
        if ((x - cnt) >= 0):
            if (board.getBoard()[x - cnt][y] != patern[cnt]):
                return (False)
        else:
            return (False)
    return (True)

def match_diag_right(board, patern, x, y):
    size = board.getSizeBoard()
    for cnt in range(len(patern)):
        if ((cnt + x) < size and (cnt + y) < size):
            if (board.getBoard()[cnt + x][y + cnt] != patern[cnt]):
                return (False)
        else:
            return (False)
    return (True)

def match_diag_left(board, patern, x, y):
    size = board.getSizeBoard()
    for cnt in range(len(patern)):
        if ((cnt + x) < size and (y - cnt) >= 0):
            if (board.getBoard()[cnt + x][y - cnt] != patern[cnt]):
                return (False)
        else:
            return (False)
    return (True)

def match_down(board, patern, x, y):
    size = board.getSizeBoard()
    for cnt in range(len(patern)):
        if ((y + cnt) < size):
            if (board.getBoard()[cnt][y + cnt] != patern[cnt]):
                return (False)
        else:
            return (False)
    return (True)

def is_matching_pattern(board, paternsType):
    for patern in paternsType:
        for x in range(board.getSizeBoard()):
            for y in range(board.getSizeBoard()):
                if (match_right(board, patern, x, y) == True):
                    print("MATCH", flush=True)
                    return (True, x, y)
                # if (match_left(board, patern, x, y) == True):
                #     print("MATCH", flush=True)
                #     return (True, x, y)
                # if (match_diag_right(board, patern, x, y) == True):
                #     print("MATCH", flush=True)
                #     return (True, x, y)
                # if (match_diag_left(board, patern, x, y) == True):
                #     print("MATCH", flush=True)
                #     return (True, x, y)
                # if (match_down(board, patern, x, y) == True):
                #     print("MATCH", flush=True)
                #     return (True, x, y)
    print("PAS DE MATCH", flush=True)
    return (False, -1, -1)