from typing import List, Optional, Tuple
import typing


# Method: Search space reduction
# Time: O(m + n), where m, n dimensions of input matrix
# Space: O(1)

def get_at(arr: List[List[int]], point: Tuple[int, int]) -> int:
    px, py = point
    return arr[px][py]


def matrix_search(arr: List[List[int]], target: int) -> Optional[tuple]:
    rows = len(arr)
    cols = len(arr[0])

    row_now = rows-1
    col_now = 0
    while 0 < row_now and col_now < cols:
        elem_now = get_at(arr, (row_now, col_now))
        # print(f"Looking at {row_now:3}:{col_now:3}, of elem {elem_now}")

        if elem_now == target:
            return row_now, col_now
        elif elem_now < target:
            col_now += 1
        else:
            row_now -= 1


# The following functions were used in the old version (looking in quadrants)
# An example of the Master theorem for figuring out complexity


def matrix_bin_search_quadrants(arr: List[List[int]], t: int) -> Optional[tuple]:
    n = len(arr)-1
    m = len(arr[0])-1
    return mbs(arr, 0, n, 0, m, t)


def check_square(matrix, x_low, x_high, y_low, y_high, target) -> Optional[tuple]:
    checking_positions = [(x, y) for x in (x_low, x_high)
                          for y in (y_low, y_high)]
    for poz in checking_positions:
        if get_at(matrix, poz) == target:
            return poz


def mbs(matrix, 
        x_low, x_high, 
        y_low, y_high, 
        target):
    print(
        f"Looking within [x:{x_low}, y: {y_low}]\t-> [x:{x_high}, y:{y_high}]")

    if x_low > x_high or y_low > y_high:
        return None

    x_mid = (x_low + x_high) // 2
    y_mid = (y_low + y_high) // 2

    up_point = (x_low, y_mid)
    left_point = (x_mid, y_low)

    mid_point = (x_mid, y_mid)

    if target == get_at(matrix, up_point):
        return up_point
    elif target == get_at(matrix, left_point):
        return left_point
    elif target == get_at(matrix, mid_point):
        return mid_point

    # Lower right
    if target > get_at(matrix, mid_point):
        # print(f"Going low right with new mid-mid-point {mmp}")
        if mid_point[0] == x_low and mid_point[1] == y_low:
            return check_square(matrix, x_low, x_high, y_low, y_high, target)

        return mbs(matrix,
                   mid_point[0], x_high,
                   mid_point[1], y_high,
                   target)

    # Top right and lower left
    if target > get_at(matrix, up_point):
        print("Going top left")
        r1 = mbs(matrix, x_low, mid_point[0]-1,
                 up_point[1], y_high, target)
        if r1:
            return r1
    if target > get_at(matrix, left_point):
        print("Going bot right")
        r2 = mbs(matrix, left_point[0], x_high,
                 y_low, mid_point[1]-1, target)

        if r2:
            return r2

    # Top left
    # print("Going top left")
    if not (target > get_at(matrix, up_point) or target > get_at(matrix, left_point)):
        return mbs(matrix, x_low, mid_point[0]-1, y_low, mid_point[1]-1, target)


if __name__ == "__main__":
    example1 = [[0, 5, 6, 7, 8],
                [1, 6, 7, 8, 9],
                [2, 10, 15, 12, 21],
                [3, 11, 16, 21, 22],
                [4, 12, 20, 70, 90]]

    print(matrix_bin_search_quadrants(example1, 21), matrix_search(example1, 21))
