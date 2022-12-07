from user import *

class Cpu(User):
    def choose_hand(self):
        self.hand = random.randint(1, 3)