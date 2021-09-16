from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def guess_spot(self):
        #Get random spot to attack
        guess_space = self.get_guess_space()
        #Update guess board with a hit or a miss
        self.update_guess_space(guess_space)
        #Update opponent board if the guess is a hit
        self.update_opponent_board()

    def get_guess_space(self):
        guess_row = random.randint(0, 19)
        guess_col = random.randint(0, 19)
        return [guess_row, guess_col]
