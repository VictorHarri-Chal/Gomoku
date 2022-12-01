#!/usr/bin/env python3

from board import *
from brain import *
from enum import Enum

# PATTERNS 1 : NAIVE PHASE
patternsAllyFour = ["01111", "10111", "11011", "11101", "11110"]
patternsEnemyFour = ["02222", "20222", "22022", "22202", "22220"]
patternsFour = patternsAllyFour + patternsEnemyFour

# PATTERNS 2 : EXPLORATION PHASE
patternsAllyThree = ["001110", "010110", "011010", "011100"]
patternsEnemyThree = ["002220", "020220", "022020", "022200"]
patternsThree = patternsAllyThree + patternsEnemyThree

patternsCheckAllyThree = ["11100", "01110", "00111"]
patternsCheckEnemyThree = ["22200", "02220", "00222"]

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
    #print("MD x:", x, "y:", y, flush=True)
    #print("pattern:", pattern)
    for letter in pattern:
        if (x < size):
            #print("[x][y], str(gameboard[x][y]), str(letter)", x, y, str(board.board[x][y]), str(letter), flush=True)
            if (str(board.board[x][y]) != str(letter)):
                #print("skip!", flush=True)
                return (False)
            else:
                x += 1
                #print("keepgoing!", flush=True)
        else:
            #print("skip cuz size", flush=True)
            return (False)
    return (True)

def is_matching_pattern(board, patternsType, power):
    index = power
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

def check_patterns(board, patternsType) -> int:
    count = 0
    down = False
    right = False
    diag_right = False
    for x in range(board.getSizeBoard()):
        for y in range(board.getSizeBoard()):
            for pattern in patternsType:
                if (match_right(board, pattern, x, y) == True and right == False):
                    #print("match right! with pattern:", pattern, flush=True)
                    count += 1
                    right = True
                if (match_diag_right(board, pattern, x, y) == True and diag_right == False):
                    #print("match diag right! with pattern:", pattern, flush=True)
                    count += 1
                    diag_right = True
                if (down == False):
                    if (match_down(board, pattern, x, y) == True):
                        #print("match down! with pattern:", pattern, flush=True)
                        count += 1
                        down = True
    return (count)

def evaluation(board, player) -> int:
    score = 0
    score += check_patterns(board, patternsAllyFour) * 16
    score += check_patterns(board, patternsCheckAllyThree) * 8
    score += check_patterns(board, patternsAllyTwo) * 4
    score -= check_patterns(board, patternsEnemyFour) * 16
    score -= check_patterns(board, patternsCheckEnemyThree) * 8
    score -= check_patterns(board, patternsEnemyTwo) * 4
    if (player == 2):
        score -= score * 2
    return (score)

def find_move(board, boardSize, t) -> tuple:
    x = -1
    y = -1
    value = 0
    temp = 0
    for cnt in range(boardSize):
        for count in range(boardSize):
            if (board.isCaseUsable(cnt, count) == True and is_pawn_around(board, boardSize, cnt, count, 1) == True):
                #print("case: ", cnt, ",", count, flush=True)
                board.doMove(cnt, count, 1)
                temp = evaluation(board, 1)
                board.removeMove(cnt, count)
                #print("score of " + cnt + " " + count + " :" + score, flush=True)
                if (temp > value):
                    #print("BETTER MOVE FOUND", flush=True)
                    x = cnt
                    y = count
                    value = temp
                    # print("Value = {}" .format(value), flush=True)
                board.removeMove(cnt, count)
            if t.getTime() > 4.7:
                return (x, y)
    return (x, y)