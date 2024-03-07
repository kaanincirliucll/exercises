from player import Player
from board import Board

class Game:

    def __init__(self):
        print("Welcome to Connect")

        p1 = Player("Bart","X")
        p2 = Player("Dries","Y")

        print(p1)
        print(p2)

        board = Board(7,6)

        board.print_board()

        won = False
        while not won:

            # input = 1
            selection = f"{p1.name}, pleas enter you're selection"

            # if not board.is_valid_column(column):
            #     print("")

game = Game()