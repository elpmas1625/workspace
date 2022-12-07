from user import *

class Player(User):
    def choose_hand(self):
        # handNumに文字列が入力されるとエラーになってしまう
        # この例外を適切に処理して下さい (ヒント：実際に文字列を入力してどのようなエラーが発生するのかを確認．)
        handNum = int(input("choose ur hand!   ROCK : 1  SCISSORS : 2  PAPER : 3  : "))


        if handNum < 1 or 3 < handNum:
            print("IndexError¥npls enter 1, 2 or 3")
            exit()

        self.hand = int(handNum)