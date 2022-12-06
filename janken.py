from player import *
from cpu import *
from hand import *

cnt = 0

class Janken:
    def __init__(self):
        pass

    def start(self):
        player = Player(input("Enter your name : "))
        cpu = Cpu("CPU")

        while True:
            print("Game start!")
            player.choose_hand()
            cpu.choose_hand()

            pHand = Hand(player)
            cHand = Hand(cpu)

            player.show_hand()
            cpu.show_hand()

            if pHand.winTo(cHand):
                print("you win")
                player.win_count()
            elif cHand.winTo(pHand):
                print("you lose")
                cpu.win_count()
            else:
                print("aiko")

            print("player_win : " , player.win, "cpu_win : ", cpu.win)
            if input("Continue? [Y/n]: ").lower() == 'n':
                exit()


