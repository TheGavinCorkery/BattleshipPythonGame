from Player import Player
from AI import AI

class Game:
    def __init__(self) -> None:
        self.player_boards = []
        self.players = []

    def run_game(self):
        self.make_player_boards()

        self.run_round()
        

    def make_player_boards(self):
        player_one = Player()
        self.players.append(player_one)
        player_one.my_board.place_ships()
        self.player_boards.append(player_one.my_board)
        player_two = Player()
        self.players.append(player_two)
        player_two.my_board.place_ships()
        self.player_boards.append(player_two.my_board)
        player_one.opponent_board = player_two.my_board
        player_two.opponent_board = player_one.my_board

    def run_round(self):
        self.players[0].guess_spot()

    def check_win(self):
        if self.players[0].hits == 15:
            print('Congrats! Player One Wins!')
        elif self.players[1].hits == 15:
            print('Congrats! Player Two Wins!')
    