#!/usr/bin/env python3

from board import *
from enum import Enum

# PATTERNS 1 : NAIVE PHASE
patternsAllyFour = ["01111", "10111", "11011", "11101", "11110"]
patternsEnemyFour = ["02222", "20222", "22022", "22202", "22220"]
patternsFour = patternsAllyFour + patternsEnemyFour

# PATTERNS 2 : EXPLORATION PHASE
patternsAllyThree = ["001110", "010110", "011010", "011100"]
patternsEnemyThree = ["002220", "020220", "022020", "022200"]
patternsThree = patternsAllyThree + patternsEnemyThree

patternsAllyTwo = ["11000", "01100", "00110", "00011"]
patternsEnemyTwo = ["22000", "02200", "00220", "00022"]
patternsTwo = patternsAllyTwo + patternsEnemyTwo

MATCHING = Enum('Matching', ['RIGHT', 'LEFT', 'DIAG_RIGHT', 'DIAG_LEFT', 'DOWN', 'NONE'])

def match_right(board, pattern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in pattern:
        if (y < size):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y += 1
        else:
            return (False)
    return (True)

def match_left(board, pattern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in pattern:
        if (y >= 0):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y -= 1
        else:
            return (False)
    return (True)

def match_diag_right(board, pattern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in pattern:
        if (y < size and x < size):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y += 1
                x += 1
        else:
            return (False)
    return (True)

def match_diag_left(board, pattern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in pattern:
        if (x < size and y >= 0):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                y -= 1
                x += 1
        else:
            return (False)
    return (True)

def match_down(board, pattern, x, y):
    size = board.getSizeBoard()
    gameBoard = board.getBoard()
    for letter in pattern:
        if (x < size):
            if (str(gameBoard[x][y]) != str(letter)):
                return (False)
            else:
                x += 1
        else:
            return (False)
    return (True)

def is_matching_pattern(board, patternsType):
    index = 0
    for pattern in patternsType:
        for x in range(board.getSizeBoard()):
            for y in range(board.getSizeBoard()):
                if (match_right(board, pattern, x, y) == True):
                    return (True, x, (y + index))
                if (match_left(board, pattern, x, y) == True):
                    return (True, x, (y - index))
                if (match_diag_right(board, pattern, x, y) == True):
                    return (True, (x + index), (y + index))
                if (match_diag_left(board, pattern, x, y) == True):
                    return (True, (x + index), (y - index))
                if (match_down(board, pattern, x, y) == True):
                    return (True, (x + index), y)
        index += 1
    return (False, -1, -1)