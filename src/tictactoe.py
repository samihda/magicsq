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

def game_over(board):
    return empty not in board

def print_board(board):
    for i, cell in enumerate(board, start=1):
        if (cell is empty):
            print(str(i), end=" ")
        else:
            print(cell, end=" ")

        if (i % 3 == 0):
            print()

def tictactoe():
    x_turn = True

    while not game_over(board):
        print_board(board)
        pawn = x if x_turn else o
        index = int(input(pawn + " move to: ")) - 1
        board[index] = pawn
        x_turn = not x_turn

if __name__ == '__main__':
    tictactoe()
