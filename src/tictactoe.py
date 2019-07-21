from magic import sum_combo

empty = ""
x = "X"
o = "O"

board = [empty for _ in range(9)]

def game_over(board, pawn):
    won = sum_combo([i for i, cell in enumerate(board) if cell is pawn])
    no_move = empty not in board
    return no_move or won

def print_board(board):
    for i, cell in enumerate(board, start=1):
        if (cell is empty):
            print(str(i), end=" ")
        else:
            print(cell, end=" ")

        if (i % 3 == 0):
            print()

def tictactoe():
    pawn = x
    finished = game_over(board, pawn)

    while not finished:
        print_board(board)
        index = int(input(pawn + " move to: ")) - 1
        board[index] = pawn
        finished = game_over(board, pawn)
        pawn = o if pawn is x else x

if __name__ == '__main__':
    tictactoe()
