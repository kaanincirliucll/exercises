class Board:

    def __init__(self, colums, rows):
        self.__colums = colums
        self.__rows = rows
        self.__initialize_board()

    def __initialize_board(self):
        self.__board = []
        for r in range(0, self.__rows):
            row=[]
            for c in range(0, self.__colums):
                row.append(" ")
            self.__board.append(row)
    
    def print_board(self):
        self.__print_line()
        for row in self.__board:
            self.__print_row(row)
            self.__print_line()

    def __print_line(self):
        line = " "
        line += "_" * (self.__colums * 4 - 1)
        line += " "
        return print(line)

    def __print_row(self, row):
        line = "|"
        for c in range(0,self.__colums):
            line += f" {row[c]} |"
        return print(line)

    def add_token(self, row, column, token):
        self.__board[row][column] = token

    def check_row(self, column):
        for c in range(self.__rows - 1, -1, -1):
            if self.__board[c][column] == " ":
             return c
        return -1
    
    def is_valid_column(self, column):
        return "a"

