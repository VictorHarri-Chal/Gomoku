#!/usr/bin/python3

from src.Board import *
from src.brain import *
from src.Paterns import *

# Print function with flush

def myPrint(toBePrint, myEnd):
    print(toBePrint, flush=True, end=myEnd)

# Class which contain all mandatory protocol function

class Protocol:
    
    def __init__(self):
        self.input = ""
        self.arg = []
        self.output = ""
        self.boardSize = 0
        self.gameBoard = MyBoard()

    # Read input and stock it in self.input
    
    def readInput(self):
        try:
            self.input = input()
        except:
            exit(0)

    # Print output which is in self.output
    
    def printOutput(self):
        myPrint(self.output, "")
    
    # START [VALUE] : Where value is the board size, the function return if the size is OK or NOT

    def start(self, value):
        try:
            size = int(value)
            if size < 5:
                self.output = "ERROR message - unsupported size or other error\n"
                return
            self.gameBoard.createBoard(size)
            self.boardSize = size
            self.output = "OK - everything is good\n"
        except ValueError:
            self.output = "ERROR message - unsupported size or other error\n"

    # TURN [X][Y] : Where X and Y are the position of the opponent's move, the function return the position X,Y of the player's move

    def turn(self, arg1) -> str:
        try:
            value = arg1.split(',')
            value1 = int(value[0])
            value2 = int(value[1])
            self.gameBoard.doMove(value1, value2, 2)
            res_match = is_matching_pattern(self.gameBoard, paternsAlly)
            res_match_enemy = is_matching_pattern(self.gameBoard, paternsEnemy)
            if (res_match[0] == True):
                self.gameBoard.doMove(res_match[1], res_match[2], 1)
                move = str(res_match[1] + "," + str(res_match[2]))
                self.output = move
            elif (res_match_enemy[0] == True):
                self.gameBoard.doMove(res_match_enemy[1], res_match_enemy[2], 1)
                move = str(res_match_enemy[1] + "," + str(res_match_enemy[2]))
                self.output = move
            else:
                pos = randPos(self.gameBoard, self.boardSize)
                move = str(pos[0]) + "," + str(pos[1]) + "\n"
                self.gameBoard.doMove(pos[0], pos[1], 1)
                self.output = move
        except ValueError:
            return ("ERROR")

    # BEGIN : The player have to play first, the function return the position X,Y of the player's move

    def begin(self):
        pos = randPos(self.gameBoard, self.boardSize)
        move = str(pos[0]) + "," + str(pos[1]) + "\n"
        self.gameBoard.doMove(pos[0], pos[1], 1)
        self.output = move

    # BOARD [X][Y][FIELD] : Where X and Y are position and FIELD is the player, the function have to return the position X,Y of the player's move

    def board(self):
        self.readInput()
        try:
            self.arg = self.input.split()
            nbArg = len(self.arg)
            if (nbArg == 1 and self.arg[0] == "DONE"):
                res_match = is_matching_pattern(self.gameBoard, paternsAlly)
                res_match_enemy = is_matching_pattern(self.gameBoard, paternsEnemy)
                if (res_match[0] == True):
                    self.gameBoard.doMove(int(res_match[1]), int(res_match[2]), 1)
                    move = str(res_match[1]) + "," + str(res_match[2])
                    self.output = move
                elif (res_match_enemy[0] == True):
                    self.gameBoard.doMove(int(res_match_enemy[1]), int(res_match_enemy[2]), 1)
                    move = str(res_match_enemy[1]) + "," + str(res_match_enemy[2])
                    self.output = move
                else:
                    pos = randPos(self.gameBoard, self.boardSize)
                    move = str(pos[0]) + "," + str(pos[1]) + "\n"
                    self.gameBoard.doMove(pos[0], pos[1], 1)
                    self.output = move
            elif (nbArg == 1):
                value = self.arg[0].split(',')
                pos_x = int(value[0])
                pos_y = int(value[1])
                player = int(value[2])
                self.gameBoard.doMove(pos_x, pos_y, player)
                self.board()
        except ValueError:
            self.readInput()
    
    # INFO [KEY][VALUE] : The player don't need to answer this

    def info(arg1, arg2) -> str:
        return ("")

    # END : The player have to quit as fast as possible and should not write anything more

    def end(self):
        exit(0)

    # ABOUT : The brain is expected to send some information about itself on one line. Each info must be written as keyword, equals sign, text value in quotation marks.
    #         Values should be separated by commas that can be followed by spaces.

    def about(self):
        self.output = "name=\"BBGOBB\", version=\"1.0\"\n"

    def computeInput(self):
        self.arg = self.input.split()
        nbArg = len(self.arg)
        if (self.arg[0] == "START" and nbArg == 2):
            self.start(self.arg[1])
            self.printOutput()
        elif (self.arg[0] == "TURN" and nbArg == 2):
            self.turn(self.arg[1])
            self.printOutput()
        elif (self.arg[0] == "BEGIN" and nbArg == 1):
            self.begin()
            self.printOutput()
        elif (self.arg[0] == "BOARD"):
            self.board()
            self.printOutput()
        elif (self.arg[0] == "INFO" and nbArg == 3):
            self.info(self.arg[1], self.arg[2])
        elif (self.arg[0] == "END" and nbArg == 1):
            self.end()
        elif (self.arg[0] == "ABOUT" and nbArg == 1):
            self.about()
            self.printOutput()
        elif (self.arg[0] == "DISPLAY"):
            self.gameBoard.displayBoard()