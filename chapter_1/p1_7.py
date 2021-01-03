from typing import List

# Method: Recursive edge-walking
# Time: O(n*m), where n,m the dimensions of the matrix
# Space: O(1)


def rotate(arr: List[List[int]]) -> List[List[int]]:
    rot_help(arr, 0, len(arr[0])-1, 0, len(arr)-1)
    return arr


def rot_help(arr, xl, xh, yl, yh):
    if xl >= xh and yl >= yh:
        print(f"Shorting 0 or 1 wide at {xl} to {xh}")
        return
    else:
        rot_help(arr, xl+1, xh-1, yl+1, yh-1)

        side = xh-xl
        for i in range(side):
            print(f"{i} of {side} side, w/ x:{xl}-{xh} y:{yl}-{yh}")
            temp = arr[yl][xl+i]  # Top left segment
            arr[yl][xl+i] = arr[yh-i][xl]  # Trasition 1
            arr[yh-i][xl] = arr[yh][xh-i]  # Transition 2
            arr[yh][xh-i] = arr[yl+i][xh]  # Transition 3
            arr[yl+i][xh] = temp  # Top right end


if __name__ == "__main__":
    ex1 = [[1, 2, 3],
           [8, 0, 4],
           [7, 6, 5]]
    rotate(ex1)
    for line in ex1:
        print(line)

    ex2 = [[1, 2], [3, 4]]
    rotate(ex2)
    for line in ex2:
        print(line)
