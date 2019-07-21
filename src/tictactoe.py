magic_square = [
    2, 7, 6,
    9, 5, 1,
    4, 3, 8,
]

empty = ""
x = "X"
o = "O"

cells = [empty, x, o]

board = [empty for _ in range(9)]

def print_board(board):
    for i, cell in enumerate(board, start=1):
        if (cell is empty):
            print(str(i), end=" ")
        else:
            print(cell, end=" ")

def tictactoe():
    print_board(board)

if __name__ == '__main__':
    tictactoe()
