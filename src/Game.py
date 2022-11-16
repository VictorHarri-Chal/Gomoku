#!/usr/bin/env python3

from src.Protocol import *

class Game:
    def __init__(self):
        self.tmp = True
        self.protocol = Protocol()
        
    def run(self):
        while (1):
            self.protocol.readInput()
            self.protocol.computeInput()