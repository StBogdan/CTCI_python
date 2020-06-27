from typing import List


def robot_br(m: List[List[int]], r, c) -> List:
    rm = [[None for _ in range(c)] for _ in range(r)]

    def up_left_rec(i, j, dir):
        if 0 > i or j < 0:
            return

        if rm[i][j] is None:
            rm[i][j] = dir
            up_left_rec(i-1, j, "u")
            up_left_rec(i, j-1, "l")

    for i in range(r):
        for j in range(c):
            if m[i][j]:
                rm[i][j] = "b"
    up_left_rec(r-1, c-1, "e")

    if not rm[0][0]:
        return []

    path = [(0, 0)]
    i, j = 0, 0
    while rm[i][j] != "e":
        dir = rm[i][j]
        if dir == "u":
            i += 1
        elif dir == "l":
            j += 1

        path.append((i, j))
    for line in rm:
        print(line)

    return path


if __name__ == "__main__":
    ex1 = [[0, 1, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 0, 0, 0],
           ]

    r, c = len(ex1), len(ex1[0])
    print(f"For the input ,result path is {robot_br(ex1, r, c)}")
