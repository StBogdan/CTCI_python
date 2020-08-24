from typing import List, Tuple


def precomp_down_left_squares(m: List[List[int]]) \
        -> Tuple[List[List[int]], List[List[int]]]:
    rows = len(m)
    cols = len(m[0])

    down_sq = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    right_sq = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

    for row in range(rows-1, -1, -1):
        for col in range(cols-1, -1, -1):
            down_sq[row][col] = 0 if m[row][col] == 0 else 1 + \
                down_sq[row+1][col]
            right_sq[row][col] = 0 if m[row][col] == 0 else 1 + \
                right_sq[row][col+1]

    return down_sq, right_sq


def check_square(coords: tuple, sq_size: int,
                 down_sq: List[List[int]],
                 right_sq: List[List[int]]) -> bool:
    """ Check that the square has squares for all the sides, as required by the the size
    l     r
    # # # # top
    #     #
    #     #
    # # # # bot
    <-----> sq_size
    """
    top_left_col, top_left_row = coords
    bot_left_col, bot_left_row = top_left_col, top_left_row + sq_size-1
    top_right_col, top_right_row = top_left_col + sq_size - 1, top_left_row

    if down_sq[top_left_row][top_left_col] < sq_size \
            or right_sq[top_left_row][top_left_col] < sq_size:
        return False

    if down_sq[top_right_row][top_right_col] < sq_size \
            or right_sq[bot_left_row][bot_left_col] < sq_size:
        return False

    return True


def max_square_outline(matrix: List[List[int]]) -> List[tuple]:
    # Return the 4 coordonates, zero-indexed
    n = len(matrix)
    down_sq, right_sq = precomp_down_left_squares(matrix)

    for square_size in range(n, 0, -1):
        for row in range(0, n-square_size+1):
            for col in range(0, n-square_size+1):
                if check_square((row, col), square_size, down_sq, right_sq):
                    return [
                        (row, col),
                        (row+square_size - 1, col + square_size - 1)
                    ]

    return []


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 1]]

    print(f"Max square in test matrix is {max_square_outline(matrix)}")
