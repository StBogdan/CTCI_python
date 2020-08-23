
from typing import List
from collections import namedtuple

ArrLargestSum = namedtuple("ArrLargestSum", "sum indexes")


def largest_submatrix_sum(m: List[List[int]]) -> None:

    rows = len(m)
    cols = len(m[0])

    max_now = -float("inf")
    row_max_now = (0, 0)
    col_max_now = (0, 0)

    for i in range(rows):
        col_sums = [0] * cols
        for j in range(i, rows):
            for col in range(cols):
                col_sums[col] += m[j][col]

            max_sum, (start_col, end_col) = get_largest_sum(col_sums)

            # print(f"Rows {i} to {j}, max is between cols {start_col} and {end_col} as {max_sum}")

            if max_sum > max_now:
                max_now = max_sum
                row_max_now = (i, j)
                col_max_now = (start_col, end_col)

    for i in range(row_max_now[0], row_max_now[1]+1):
        print()
        for j in range(col_max_now[0], col_max_now[1]+1):
            print(f"{m[i][j]:3}", end=" ")


def precomp_matrix_sums(m: List[List[int]]) -> List[List[int]]:
    rows = len(m)
    cols = len(m[0])
    # Add padding
    sum_m = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            elem_here = m[row-1][col-1]
            sum_m[row][col] = sum_m[row-1][col] + \
                sum_m[row][col-1] - sum_m[row-1][col-1] + elem_here

    for line in sum_m:
        print(line)

    print("-"*50)

    trimmed_arr = [x[1:] for x in sum_m[1:]]
    for line in trimmed_arr:
        print(line)

    return trimmed_arr


def get_largest_sum(arr: List[int]):
    csum = 0
    cstart = 0

    max_sum = -float("inf")
    max_inds = (0, 0)

    for i in range(len(arr)):
        elem = arr[i]
        csum += elem

        if csum > max_sum:
            max_sum = csum
            max_inds = (cstart, i)

        if csum < 0:
            csum = 0
            cstart = i+1  # It at least going to be the next

    return ArrLargestSum(max_sum, max_inds)


if __name__ == "__main__":
    test_matrix = [
        [1, 2, 3, 4, 5],
        [2, 3, -5000, 5, 6],
        [10, 20, 30, 40, 50],
    ]

    test_matrix_2 = [[1, -2, -1, 4],
                     [1, -1, 1, 1],
                     [0, -1, -1, 1],
                     [0, 0, 1, 1]]

    largest_submatrix_sum(test_matrix_2)
