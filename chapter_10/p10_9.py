from typing import List, Optional


def matrix_bin_search(arr: List[List[int]], t: int) -> Optional[tuple]:
    n = len(arr)-1
    m = len(arr[0])-1
    return mbs(arr, 0, n, 0, m, t)


def gat(arr, point):
    px, py = point
    return arr[px][py]


def check_square(a, xl, xh, yl, yh, t) -> Optional[tuple]:
    poss = [(x, y) for x in (xl, xh) for y in (yl, yh)]
    for poz in poss: 
        if gat(a, poz) == t:
            return poz


def mbs(a, xl, xh, yl, yh, t):
    print(f"Looking within [x:{xl}, y: {yl}]\t-> [x:{xh}, y:{yh}]")

    if xl > xh or yl > yh:
        return None

    xm = (xl + xh) // 2
    ym = (yl + yh) // 2

    upp = (xl, ym)
    leftp = (xm, yl)

    mmp = (xm, ym)

    if t == gat(a, upp):
        return upp
    elif t == gat(a, leftp):
        return leftp
    elif t == gat(a, mmp):
        return mmp

    # Lower right
    if t > gat(a, mmp):
        print(f"Going low right with new mmp {mmp}")
        if mmp[0] == xl and mmp[1] == yl:
            return check_square(a, xl, xh, yl, yh, t)

        return mbs(a, mmp[0], xh, mmp[1], yh, t)

    # Top right and lower left
    if t > gat(a, upp):
        print("Going top left")
        r1 = mbs(a, xl, mmp[0]-1,
                 upp[1], yh, t)
        if r1:
            return r1
    if t > gat(a, leftp):
        print("Going bot right")
        r2 = mbs(a, leftp[0], xh,
                 yl, mmp[1]-1, t)

        if r2:
            return r2

    # Top left
    print("Going top left")
    if not (t > gat(a, upp) or t > gat(a, leftp)):
        return mbs(a, xl, mmp[0]-1, yl, mmp[1]-1, t)


if __name__ == "__main__":
    example1 = [[0, 5, 6, 7, 8],
                [1, 6, 7, 8, 9],
                [2, 10, 15, 120, 21],
                [3, 11, 16, 21, 22],
                [4, 12, 20, 70, 90]]

    print(matrix_bin_search(example1, 21))
