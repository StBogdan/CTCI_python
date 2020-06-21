from typing import List


def zero_m(matric: List[List[int]]):
    n, m = len(matric), len(matric[0])
    fcol0 = False
    frow0 = False

    for i in range(n):
        if matric[i][0] == 0:
            fcol0 = True
            break

    for j in range(m):
        if matric[0][j] == 0:
            frow0 = True
            break

    for i in range(n):
        for j in range(m):
            if matric[i][j] == 0:
                matric[i][0] = 0
                matric[0][j] = 0

    print(f"Gonna zero now, first row {frow0} and first col {fcol0}")
    mrint(matric)

    for i in range(1, n):
        if matric[i][0] == 0:
            for j in range(m):
                matric[i][j] = 0

    for j in range(1, m):
        if matric[0][j] == 0:
            for i in range(n):
                matric[i][j] = 0

    if fcol0:
        for i in range(n):
            matric[i][0] = 0

    if frow0:
        for j in range(m):
            matric[0][j] = 0

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
