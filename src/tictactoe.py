magic_square = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8],
]

board = magic_square

def print_board(board):
    for row in board:
        for col in row:
            print(str(col), end=" ")
        print()

def tictactoe():
    print_board(board)

if __name__ == '__main__':
    tictactoe()
