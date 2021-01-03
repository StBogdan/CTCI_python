from typing import List

# Method: Individual cell checks, with handling of first line and col
# Time: O(n*m)
# Space: O(1)


def zero_m(matric: List[List[int]]):
    rows, cols = len(matric), len(matric[0])
    fcol0 = False
    frow0 = False

    for r in range(rows):
        if matric[r][0] == 0:
            fcol0 = True
            break

    for c in range(cols):
        if matric[0][c] == 0:
            frow0 = True
            break

    for r in range(rows):
        for c in range(cols):
            if matric[r][c] == 0:
                matric[r][0] = 0
                matric[0][c] = 0

    print(f"Gonna zero now, first row {frow0} and first col {fcol0}")
    mrint(matric)

    for r in range(1, rows):
        if matric[r][0] == 0:
            for c in range(cols):
                matric[r][c] = 0

    for c in range(1, cols):
        if matric[0][c] == 0:
            for r in range(rows):
                matric[r][c] = 0

    if fcol0:
        for r in range(rows):
            matric[r][0] = 0

    if frow0:
        for c in range(cols):
            matric[0][c] = 0

    return matric


def mrint(matrix: List[List[int]]):
    for line in matrix:
        print(line)


if __name__ == "__main__":
    ex1 = [[1, 2, 3],
           [8, 0, 4],
           [7, 6, 5]]

    mrint(zero_m(ex1))
    print("-"*50)
    ex2 = [[0, 1, 2],
           [4, 5, 6]]

    mrint(zero_m(ex2))
