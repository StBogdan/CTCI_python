from collections import defaultdict
import time

DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def update_bounds(elem, bounds):
    if elem > bounds[1]:
        bounds[1] = elem
    elif elem < bounds[0]:
        bounds[0] = elem


def print_k_moves(k: int):
    matrix = defaultdict(lambda: 0)

    dir_index = 0
    row = 0
    col = 0
    row_bounds = [0, 0]
    col_bounds = [0, 0]

    for i in range(k):
        square_now = matrix[(row, col)]

        if square_now:
            matrix[(row, col)] = 0
            dir_index -= 1
        else:
            matrix[(row, col)] = 1
            dir_index += 1

        dir_index %= len(DIRS)

        drow, dcol = DIRS[dir_index]
        row += drow
        col += dcol

        update_bounds(row, row_bounds)
        update_bounds(col, col_bounds)

    for i in range(row_bounds[0], row_bounds[1]+1):
        for j in range(col_bounds[0], col_bounds[1]+1):
            print("░" if not matrix[(i, j)] else "█", end="")
        print()


if __name__ == "__main__":
    # for i in range(11005):
    #     print_k_moves()
    #     print("-"*50)

    print_k_moves(12_000)
