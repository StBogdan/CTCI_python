from typing import List


def queens_8():
    current_queens = []
    ways = 0
    for i in range(8):
        ways += rec_queen_place(1, [(i, 0)])

    return ways


def rec_queen_place(col: int, queen_list):
    # print(f"Current queens {queen_list}")
    if col >= 8:
        display_queen_placement(queen_list)
        return 1

    possible_rows = set(range(8))
    for (qr, qc) in queen_list:
        possible_rows.remove(qr)

    ways = 0
    for row in possible_rows:
        if valid_w_queens((row, col), queen_list):
            ways += rec_queen_place(col+1, queen_list + [(row, col)])
    return ways


def valid_w_queens(poz, queens):
    diag_desc = poz[0]-poz[1]
    diag_asc = poz[0] + poz[1]
    return not any(qi-qj == diag_desc or qi+qj == diag_asc
                   for (qi, qj) in queens)


def display_queen_placement(ql: List):
    board = [['_' for _ in range(8)] for _ in range(8)]
    for qi, qj in ql:
        board[qi][qj] = "Q"

    for line in board:
        print(line)
    print("-"*50)

if __name__ == "__main__":
    print(f"Got ways to put 8 queens: {queens_8()}")
