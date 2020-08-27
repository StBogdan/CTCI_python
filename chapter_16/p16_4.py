from typing import List, Optional
from enum import Enum


class Dir(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)
    UPRIGHT = (-1, 1)
    UPLEFT = (-1, -1)
    DOWNRIGHT = (1, 1)
    DOWNLEFT = (1, -1)


def check_in_dir(m: List[List[chr]],
                 start_poz: tuple,
                 direction: Dir) -> Optional[chr]:
    sr, sc = start_poz
    dr, dc = direction.value
    winner_sign = m[sr][sc]
    # print(f"Checking from {start_poz}, going in dir {dr} {dc}, {winner_sign}")

    # If not complete on this direction, no winner
    if not winner_sign:
        return None

    row = sr
    col = sc
    while 0 <= row < len(m) and 0 <= col < len(m[0]):
        elem_now = m[row][col]
        if elem_now != winner_sign:
            return None
        row += dr
        col += dc

    return winner_sign


def check_xo(board: List[List[chr]]):
    rows = len(board)
    cols = len(board[0])

    row_winners = [check_in_dir(board, (row, 0), Dir.RIGHT)
                   for row in range(rows)]

    col_winners = [check_in_dir(board, (0, col), Dir.DOWN)
                   for col in range(cols)]

    diag_winners = [check_in_dir(board, (0, 0), Dir.DOWNRIGHT),
                    check_in_dir(board, (0, cols-1), Dir.DOWNLEFT)]

    # print(f"Row winners {row_winners}, "
    #   f"col {col_winners} and diags: {diag_winners}")

    possible_winners = set(x for x in row_winners +
                           col_winners + diag_winners if x)
    if len(possible_winners) > 1:
        raise Exception("Contested board detected")
    else:
        return list(possible_winners)[0]


if __name__ == "__main__":
    board = [
        ['x', 'o', 'o'],
        ['o', 'o', 'o'],
        ['x', 'o', 'x']
    ]
    winrar = check_xo(board)
    print(f"Winner of the board is {winrar}")
