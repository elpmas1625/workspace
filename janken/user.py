import random

HANDS = {1: "rock", 2: "scissors", 3: "paper"}

class User:
    def __init__(self, name):
        self.name = name
        self.hand = 0
        self.win = 0

    def win_count(self):
        self.win += 1

    def show_hand(self):
        print(self.name , " : ", HANDS[self.hand])

