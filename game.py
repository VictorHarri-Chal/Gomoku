#!/usr/bin/env python3

import sys
from protocol import *

class Game:
    def __init__(self):
        self.tmp = True
        self.protocol = Protocol()
        
    def run(self):
        try:
            if len(sys.argv) == 2:
                file = open(sys.argv[1], "r")
                while (True):
                    self.protocol.readInput(sys.argv, file)
                    self.protocol.computeInput(sys.argv, file)
            elif len(sys.argv) == 1:
                file = ""
                while (True):
                    self.protocol.readInput(sys.argv, file)
                    self.protocol.computeInput(sys.argv, file)
        except:
            exit(0)