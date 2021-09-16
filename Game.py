from Player import Player
from AI import AI

class Game:
    def __init__(self) -> None:
        self.player_boards = []
        self.players = []
        self.is_winner = False

    def run_game(self):
        self.display_welcome()
        self.make_player_boards()
        while self.is_winner == False:
            self.run_round()
        
        
    def exit_game(self):
        print('\n------------------------------------------')
        print('Thank you for playing. I hope you enjoyed!')
    
    def display_welcome(self):
        print('Welcome to Battleship!')
        print('The goal is to destroy all of your opponents ships before losing all of yours!')
        print('There is no cheating...  if it is not your turn, LOOK AWAY <3')
        print('----------------------------------------------------------')

    def make_player_boards(self):
        player_one = Player()
        self.players.append(player_one)
        print('Player one, get ready to place your ships! Player two needs to look away!')
        print('----------------------------------------------------------')
        player_one.my_board.place_ships()
        self.player_boards.append(player_one.my_board)
        print('Player two, it is time to place your ships! Player one no peeking :)')
        print('----------------------------------------------------------')
        player_two = Player()
        self.players.append(player_two)
        player_two.my_board.place_ships()
        self.player_boards.append(player_two.my_board)
        player_one.opponent_board = player_two.my_board
        player_two.opponent_board = player_one.my_board

    def run_round(self):
        print('\n------------------------------')
        print('Player One, guess a spot to hit!')
        self.players[0].guess_spot()
        print('\n------------------------------')
        print('Player Two, guess a spot to hit!')
        self.players[1].guess_spot()
        self.check_win()

    def check_win(self):
        if self.players[0].hits == 14:
            print('Congrats! Player One Wins!')
            self.is_winner == True
        elif self.players[1].hits == 14:
            print('Congrats! Player Two Wins!')
            self.is_winner == True
    