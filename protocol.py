#!/usr/bin/python3

from patterns import *
from board import *
from brain import *
from timer import *

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
        self.isStart = True

    # Read input and stock it in self.input
    
    def readInput(self, args, file):
        if len(args) == 2:
            self.input = file.readline()
            print("DEBUG " + self.input)
        elif len(args) == 1:
            self.input = input()
            print("DEBUG " + self.input)

    # Print output which is in self.output
    
    def printOutput(self):
        myPrint(self.output, "")
    
    # START [VALUE] : Where value is the board size, the function return if the size is OK or NOT

    def start(self, value):
        try:
            size = int(value)
            if size < 5:
                self.output = "ERROR wrong size\n"
                return
            self.gameBoard.createBoard(size)
            self.boardSize = size
            self.output = "OK\n"
        except ValueError:
            self.output = "ERROR can't create the board\n"

    # TURN [X][Y] : Where X and Y are the position of the opponent's move, the function return the position X,Y of the player's move

    def turn(self, arg1) -> str:
        try:
            # t = Timer()
            # t.start()if (self.isStart == True):
            value = arg1.split(',')
            value1 = int(value[0])
            value2 = int(value[1])
            self.gameBoard.doMove(value1, value2, 2)
            res_match = is_matching_pattern(self.gameBoard, patternsAllyFour, 0)
            res_match_enemy = is_matching_pattern(self.gameBoard, patternsEnemyFour, 0)
            res_match3 = is_matching_pattern(self.gameBoard, patternsAllyThree, 1)
            res_match_enemy3 = is_matching_pattern(self.gameBoard, patternsEnemyThree, 1)
            if (res_match[0] == True):
                self.gameBoard.doMove(res_match[1], res_match[2], 1)
                move = str(res_match[1]) + "," + str(res_match[2])
                self.output = move + "\n"
            elif (res_match_enemy[0] == True):
                self.gameBoard.doMove(res_match_enemy[1], res_match_enemy[2], 1)
                move = str(res_match_enemy[1]) + "," + str(res_match_enemy[2])
                self.output = move + "\n"
            elif (res_match3[0] == True):
                self.gameBoard.doMove(res_match3[1], res_match3[2], 1)
                move = str(res_match3[1]) + "," + str(res_match3[2])
                self.output = move + "\n"
            elif (res_match_enemy3[0] == True):
                self.gameBoard.doMove(res_match_enemy3[1], res_match_enemy3[2], 1)
                move = str(res_match_enemy3[1]) + "," + str(res_match_enemy3[2])
                self.output = move + "\n"
            else:
                if (self.isStart == True):
                    pos = (self.boardSize - 1) / 2
                    pos = pos.__round__()
                    if (self.gameBoard.board[pos][pos] == 0):
                        self.gameBoard.doMove(pos, pos, 1)
                        self.output = str(pos) + ","  + str(pos) + "\n"
                        self.isStart = False
                    else:
                        self.gameBoard.doMove(int(pos), int(pos), 1)
                        self.output = str(pos) + ","  + str(pos) + "\n"
                        self.isStart = False
                    return
                pos = find_move(self.gameBoard, self.boardSize)
                # pos = randPos(self.gameBoard, self.boardSize)
                move = str(pos[0]) + "," + str(pos[1]) + "\n"
                self.gameBoard.doMove(pos[0], pos[1], 1)
                self.output = move
            # self.gameBoard.displayBoard()
            # t.stop()
        except ValueError:
            return ("ERROR turn command\n")

    # BEGIN : The player have to play first, the function return the position X,Y of the player's move

    def begin(self):
        pos = (self.boardSize - 1) / 2
        pos = pos.__round__()
        self.gameBoard.doMove(pos, pos, 1)
        self.output = str(pos) + ","  + str(pos) + "\n"
        self.isStart = False

    # BOARD [X][Y][FIELD] : Where X and Y are position and FIELD is the player, the function have to return the position X,Y of the player's move

    def board(self, args, file):
        self.readInput(args, file)
        try:
            self.arg = self.input.split()
            nbArg = len(self.arg)
            if (nbArg == 1 and self.arg[0] == "DONE"):
                res_match = is_matching_pattern(self.gameBoard, patternsAllyFour, 0)
                res_match_enemy = is_matching_pattern(self.gameBoard, patternsEnemyFour, 0)
                res_match3 = is_matching_pattern(self.gameBoard, patternsAllyThree, 1)
                res_match_enemy3 = is_matching_pattern(self.gameBoard, patternsEnemyThree, 1)
                if (res_match[0] == True):
                    self.gameBoard.doMove(int(res_match[1]), int(res_match[2]), 1)
                    move = str(res_match[1]) + "," + str(res_match[2])
                    self.output = move + "\n"
                elif (res_match_enemy[0] == True):
                    self.gameBoard.doMove(int(res_match_enemy[1]), int(res_match_enemy[2]), 1)
                    move = str(res_match_enemy[1]) + "," + str(res_match_enemy[2])
                    self.output = move + "\n"
                elif (res_match3[0] == True):
                    self.gameBoard.doMove(res_match3[1], res_match3[2], 1)
                    move = str(res_match3[1]) + "," + str(res_match3[2])
                    self.output = move + "\n"
                elif (res_match_enemy3[0] == True):
                    self.gameBoard.doMove(res_match_enemy3[1], res_match_enemy3[2], 1)
                    move = str(res_match_enemy3[1]) + "," + str(res_match_enemy3[2])
                    self.output = move + "\n"
                else:
                    if (self.isStart == True):
                        pos = (self.boardSize - 1) / 2
                        pos = pos.__round__()
                        if (self.gameBoard.board[pos][pos] == 0):
                            self.gameBoard.doMove(pos, pos, 1)
                            self.output = str(pos) + ","  + str(pos) + "\n"
                            self.isStart = False
                        else:
                            self.gameBoard.doMove(int(pos), int(pos), 1)
                            self.output = str(pos) + ","  + str(pos) + "\n"
                            self.isStart = False
                        return
                    pos = find_move(self.gameBoard, self.boardSize)
                    # pos = randPos(self.gameBoard, self.boardSize)
                    move = str(pos[0]) + "," + str(pos[1]) + "\n"
                    self.gameBoard.doMove(pos[0], pos[1], 1)
                    self.output = move
            elif (nbArg == 1):
                value = self.arg[0].split(',')
                pos_x = int(value[0])
                pos_y = int(value[1])
                player = int(value[2])
                self.gameBoard.doMove(pos_x, pos_y, player)
                self.board(args, file)
        except ValueError:
            self.readInput(args, file)
    
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

    def score(self, player):
        score = 0
        score += check_patterns(self.gameBoard, patternsAllyFour) * 16
        score += check_patterns(self.gameBoard, patternsAllyThree) * 8
        score += check_patterns(self.gameBoard, patternsAllyTwo) * 4
        score -= check_patterns(self.gameBoard, patternsEnemyFour) * 16
        score -= check_patterns(self.gameBoard, patternsEnemyThree) * 8
        score -= check_patterns(self.gameBoard, patternsEnemyTwo) * 4
        if (player == 2):
            score += check_patterns(self.gameBoard, patternsEnemyFour) * 16
            score += check_patterns(self.gameBoard, patternsEnemyThree) * 8
            score += check_patterns(self.gameBoard, patternsEnemyTwo) * 4
            score -= check_patterns(self.gameBoard, patternsAllyFour) * 16
            score -= check_patterns(self.gameBoard, patternsAllyThree) * 8
            score -= check_patterns(self.gameBoard, patternsAllyTwo) * 4
        return (score)

    def computeInput(self, args, file):
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
            self.board(args, file)
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
        elif (self.arg[0] == "SCORE"):
            self.score(2)
            self.printOutput()
