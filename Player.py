from Board import Board

class Player():
    def __init__(self):
        self.my_board = Board()
        self.guess_board = Board()
        self.opponent_board = []
        self.hits = 0

    #Control all methods to guess a spot on opponents board
    def guess_spot(self):
        print('Here is your current guessing board')
        print(self.guess_board.player_board)
        guess_space = self.get_guess_space()
        #Update guess board with a hit or a miss
        hit_or_miss = self.space_hit_or_miss(guess_space)
        self.update_guess_board(guess_space, hit_or_miss)
        

    def space_hit_or_miss(self,guess_space):
        if self.opponent_board.player_board[guess_space[1]][guess_space[0]] == 'x':
            print ("Congrats, you sunk my battleship")
            self.hits += 1
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
            self.guess_board.player_board[guessed_space[1]][guessed_space[0]] = 'H'
        else:
            self.guess_board.player_board[guessed_space[1]][guessed_space[0]] = 'M'
