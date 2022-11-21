#!/usr/bin/env python3

from board import *
from enum import Enum

# PARTERNS 1 : NAIVE PHASE
paternsAlly1 = ["01111", "10111", "11011", "11101", "11110"]
paternsEnemy1 = ["02222", "20222", "22022", "22202", "22220"]
paterns1 = paternsAlly1 + paternsEnemy1

# PARTERNS 2 : EXPLORATION PHASE
paternsAlly2 = ["001110", "010110", "011010", "011100"]
paternsEnemy2 = ["002220", "020220", "022020", "022200"]
paterns2 = paternsAlly2 + paternsEnemy2

MATCHING = Enum('Matching', ['RIGHT', 'LEFT', 'DIAG_RIGHT', 'DIAG_LEFT', 'DOWN', 'NONE'])

def match_right(board, patern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in patern:
        if (y < size):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y += 1
        else:
            return (False)
    return (True)

def match_left(board, patern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in patern:
        if (y >= 0):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y -= 1
        else:
            return (False)
    return (True)

def match_diag_right(board, patern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in patern:
        if (y < size and x < size):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y += 1
                x += 1
        else:
            return (False)
    return (True)

def match_diag_left(board, patern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in patern:
        if (x < size and y >= 0):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y -= 1
                x += 1
        else:
            return (False)
    return (True)

def match_down(board, patern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in patern:
        if (x < size):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                x += 1
        else:
            return (False)
    return (True)

def is_matching_pattern(board, paternsType):
    index = 0
    for patern in paternsType:
        for x in range(board.getSizeBoard()):
            for y in range(board.getSizeBoard()):
                if (match_right(board, patern, x, y) == True):
                    return (True, x, (y + index))
                if (match_left(board, patern, x, y) == True):
                    return (True, x, (y - index))
                if (match_diag_right(board, patern, x, y) == True):
                    return (True, (x + index), (y + index))
                if (match_diag_left(board, patern, x, y) == True):
                    return (True, (x + index), (y - index))
                if (match_down(board, patern, x, y) == True):
                    return (True, (x + index), y)
        index += 1
    return (False, -1, -1)