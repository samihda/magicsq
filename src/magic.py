size = 3

square = [
    2, 7, 6,
    9, 5, 1,
    4, 3, 8,
]

constant = 15

indexes = range(size * size)

rows = [list(indexes[i:i + size]) for i in range(0, len(indexes), size)]
cols = [list(range(i, size * size, size)) for i in range(size)]
diag_1 = [i + offset for i, offset in zip(range(0, size * size, size), range(size))]
diag_2 = [i + offset for i, offset in zip(range(0, size * size, size), reversed(range(size)))]
combos = [*rows, *cols, diag_1, diag_2]

for combo in combos:
    assert(sum([square[i] for i in combo]) == constant)

def win_combo(idxs):
    for combo in combos:
        if set(combo).issubset(idxs):
            return True

    return False
