class Hand:
    def __init__(self, user):
        self.hand = user.hand

    def winTo(self, enemy):
        if enemy.hand - self.hand == 1 or enemy.hand - self.hand == -2:
            return True
        else:
            return False