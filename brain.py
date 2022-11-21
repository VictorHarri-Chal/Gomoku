#!/usr/bin/env python3

import random

def howManyPawnRightDiagonal(board, x, y) -> int:
    nb = 1
    player = board[x][y]
    cnt = x + 1
    count = y + 1
    while cnt < len(board):
        while count < len(board[cnt]):
            if (board[cnt][count] == player):
                nb += 1
            else:
                return nb
            if (board[cnt][count] == 5):
                return nb
            cnt += 1
            count += 1
    return (nb)
    
def howManyPawnLeftDiagonal(board, x, y) -> int:
    nb = 1
    player = board[x][y]
    cnt = x + 1
    count = y - 1
    while cnt < len(board):
        while count >= 0:
            if (board[cnt][count] == player):
                nb += 1
            else:
                return nb
            if (board[cnt][count] == 5):
                return nb
            cnt += 1
            count -= 1
    return (nb)

def howManyPawnRight(board, x, y) -> int:
    nb = 1
    player = board[x][y]
    cnt = x + 1
    while cnt < len(board):
        if (board[cnt][y] == player):
            nb += 1
        else:
            return nb
        if (board[cnt][y] == 5):
            return nb
        cnt += 1
    return (nb)

def howManyPawnLeft(board, x, y) -> int:
    nb = 1
    player = board[x][y]
    cnt = x - 1
    while cnt >= 0:
        if (board[cnt][y] == player):
            nb += 1
        else:
            return nb
        if (board[cnt][y] == 5):
            return nb
        cnt -= 1
    return (nb)

def randPos(board, boardSize) -> tuple:
    x = random.randint(0, boardSize)
    y = random.randint(0, boardSize)
    while (board.isCaseUsable(x, y) == False):
        x = random.randint(0, boardSize)
        y = random.randint(0, boardSize)
    return (x, y)
    
def isWinnable(board, player) -> str:
    for cnt in range(len(board)):
        for count in range(len(board[cnt])):
            if (board[cnt][count] == player):
                return
    return (str(-1) + ',' + str(-1))

def isLosable(board, player) -> str:
    
    return (str(-1) + ',' + str(-1))