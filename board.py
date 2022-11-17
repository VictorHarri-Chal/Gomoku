#!/usr/bin/python3

from brain import *

class MyBoard:
    
    def __init__(self):
        board = []
        boardSize = 0
       
    def createBoard(self, size):
        self.boardSize = size
        self.board = [[0 for j in range(size)] for i in range(size)]
        
    def displayBoard(self):
        cnt = 0
        while (cnt < self.boardSize):
            print(self.board[cnt])
            cnt += 1
            
    def getBoard(self):
        return (self.board)
    
    def doMove(self, x, y, player):
        if (self.isCaseUsable(x, y) == True):
            self.board[x][y] = player
                
    def isCaseUsable(self, x, y) -> bool:
        if (x < self.boardSize and y < self.boardSize and x >= 0 and y >= 0):
            if (self.board[x][y] == 0):
                return (True)
        return (False)