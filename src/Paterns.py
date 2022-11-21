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