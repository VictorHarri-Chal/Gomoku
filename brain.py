#!/usr/bin/env python3

import random
from board import *
from patterns import *

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

def is_pawn_around(board, boardSize, x, y, player) -> bool:
    if ((x + 1) < boardSize):
        if (board.board[x + 1][y] == player):  # DROITE
            return (True)
    if ((x - 1) >= 0):
        if (board.board[x - 1][y] == player):  # GAUCHE
            return (True)
    if ((y - 1) >= 0):
        if (board.board[x][y - 1] == player): # HAUT
            return (True)
    if ((y + 1) < boardSize):
        if (board.board[x][y + 1] == player): # BAS
            return (True)
    if ((x + 1) < boardSize and (y + 1) < boardSize): # BAS DROITE
        if (board.board[x + 1][y + 1] == player):
            return (True)
    if ((x + 1) < boardSize and (y - 1) >= 0):
        if (board.board[x + 1][y - 1] == player): # HAUT DROITE
            return (True)
    if ((x - 1) > 0 and (y + 1) < boardSize):
        if (board.board[x - 1][y + 1] == player): # BAS GAUCHE
            return (True)
    if ((x - 1) >= 0 and (y - 1) >= 0):
        if (board.board[x - 1][y - 1] == player):  # HAUT GAUCHE
            return (True)
