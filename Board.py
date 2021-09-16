class Board:
    def __init__(self):
        self.player_board = []
        self.create_board()

    def create_board(self):
        for i in range(20):
            col = []
            for j in range(20):
                col.append('o')
            self.player_board.append(col)

    def create_ai_board(self):
        pass
    
    def print_board(self):
        for row in self.player_board:
            print(' '.join(row))

    def place_ships(self):
        self.place_destroyer()
        self.place_submarine()
        self.place_battleships()
        self.place_aircraft_carrier()
    
    def place_destroyer(self):
        print('Placing destroyer, you must choose two places that touch each other to place the ship')
        for x in range(1, 3):
            ship_col = int(input(f'Which column out of 20 do you want to place the {x} part of ship?'))
            ship_row = int(input(f'Which row out of 20 do you want to place the {x} part of ship?'))
            self.player_board[ship_row][ship_col] = 'x'
        self.print_board()

    def place_submarine(self):
        print('Placing submarine, you must choose three places that touch each other to place the ship')
        for x in range(1, 4):
            ship_col = int(input(f'Which column out of 20 do you want to place the {x} part of ship?'))
            ship_row = int(input(f'Which row out of 20 do you want to place the {x} part of ship?'))
            self.player_board[ship_row - 1][ship_col - 1] = 'x'
        self.print_board()

    def place_battleships(self):
        print('Placing battleship, you must choose four places that touch each other to place the ship')
        for x in range(1, 5):
            ship_col = int(input(f'Which column out of 20 do you want to place the {x} part of ship?'))
            ship_row = int(input(f'Which row out of 20 do you want to place the {x} part of ship?'))
            self.player_board[ship_row - 1][ship_col - 1] = 'x'
        self.print_board()

    def place_aircraft_carrier(self):
        print('Placing aircraft carrier, you must choose five places that touch each other to place the ship')
        for x in range(1, 6):
            ship_col = int(input(f'Which column out of 20 do you want to place the {x} part of ship?'))
            ship_row = int(input(f'Which row out of 20 do you want to place the {x} part of ship?'))
            self.player_board[ship_row - 1][ship_col - 1] = 'x'
        self.print_board()


