size = 3

square = [
    2, 7, 6,
    9, 5, 1,
    4, 3, 8,
]

constant = 15

def win_combo(indexes):
    total = 0
    for n in [square[i] for i in indexes]:
        total += n

    return total == constant
