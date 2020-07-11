
from typing import List

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def paint_fill(img: List[List[int]], point: tuple, color: int) -> None:
    fill_rec(img, point, gp(img, point), color)


def gp(matrix, point):
    x, y = point
    return matrix[x][y]


def fill_rec(img,  point, from_c, to_c):
    if gp(img, point) == from_c:
        x, y = point
        img[x][y] = to_c
        for xd, yd in DIRS:
            nx, ny = xd + x, yd + y

            if 0 <= nx and nx < len(img) and 0 <= ny and ny < len(img[0]):
                fill_rec(img, (nx, ny), from_c, to_c)


if __name__ == "__main__":
    ex = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 3, 3, 3, 1, 1, 1],
          [1, 1, 1, 2, 1, 2, 1, 1, 1],
          [1, 1, 1, 2, 1, 2, 1, 1, 1],
          [1, 1, 1, 2, 1, 2, 1, 1, 1]]

    loc3 = (1, 3)
    paint_fill(ex, loc3, 2)

    for line in ex:
        print(line)
