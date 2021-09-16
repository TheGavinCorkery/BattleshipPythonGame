from Board import Board

class Player():
    def __init__(self):
        self.my_board = Board()
        self.guess_board = Board()
        self.opponent_board = []

    #Control all methods to guess a spot on opponents board
    def guess_spot(self):
        guess_space = self.get_guess_space()
        #Update guess board with a hit or a miss
        hit_or_miss = self.space_hit_or_miss(guess_space)
        self.update_guess_board(guess_space, hit_or_miss)
        

    def space_hit_or_miss(self,guess_space):
        if self.opponent_board.player_board[guess_space[0]][guess_space[1]] == 'x':
            print ("Congrats, you sunk my battleship")
            return True
        else:
            print('You missed!')
            return False

    #Method to get input from user on their space to guess and returns it as a list
    def get_guess_space(self):
        guess_row = int(input('What row do you want to guess?: '))
        guess_col = int(input('What column do you want to guess?: '))
        return [guess_row, guess_col]

    def update_guess_board(self, guessed_space, did_it_hit):
        if did_it_hit == True:
            self.guess_board.player_board[guessed_space[0]][guessed_space[1]] = 'X'
        else:
            self.guess_board.player_board[guessed_space[0]][guessed_space[1]] = 'M'
