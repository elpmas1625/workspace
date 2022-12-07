from player import *
from cpu import *
from hand import *


class Janken:
    def __init__(self):
        pass

    def start(self):
        pName = input("Enter your name : ")
        # Playerクラスからインスタンスを生成してみよう．(ヒント：下のCpuクラスの場合を参考に)
        # player = 

        # Cpuクラスからcpuインスタンスを生成
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
                print("YOU WIN!")
                player.win_count()
            elif cHand.winTo(pHand):
                print("YOU LOSE...")
                cpu.win_count()
            else:
                print("Draw!")

            print("player_win : " , player.win, "cpu_win : ", cpu.win)


            while True:
                # 入力値に ".lower()" を使用している理由を考えよう．下の"A."に追記しよう．(ヒント：入力者に対する配慮)
                # A.
                cont = input("Continue? [Y/n]: ").lower()
                if cont == 'n':
                    exit()
                elif cont == 'y':
                    break
                else:
                    print("pls enter 'y' or 'n'")

            print("===================================================")
