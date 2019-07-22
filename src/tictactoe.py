from magic import win_combo

empty = ""
x = "X"
o = "O"

board = [empty for _ in range(9)]

def move_valid(board, index):
    if not (0 <= index < len(board)):
        return False

    return index in [i for i, cell in enumerate(board) if cell is empty]

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

    while empty in board:
        print_board(board)

        input_string = ""
        try:
            input_string = input(pawn + " move to: ")
        except (KeyboardInterrupt, EOFError):
            print()
            exit(0)

        index = -1
        try:
            index = int(input_string) - 1
        except ValueError:
            print("Please enter a number\n")
            continue

        if (move_valid(board, index)):
            board[index] = pawn
        else:
            print("Invalid move\n")
            continue

        if (win_combo([i for i, cell in enumerate(board) if cell is pawn])):
            print()
            print_board(board)
            print(x + " won")
            break

        pawn = o if pawn is x else x
        print()

if __name__ == '__main__':
    tictactoe()
