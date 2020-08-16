from typing import List


def get_lake_volumes(arr: List[int]) -> int:
    n = len(arr)
    left_bigger = [0]*n
    right_bigger = [0]*n

    bigger_left_now = 0
    bigger_right_now = 0
    for i in range(n):
        elem = arr[i]
        if elem > bigger_left_now:
            bigger_left_now = elem
        else:
            left_bigger[i] = bigger_left_now

        j = n-1-i
        elem_end = arr[j]

        if elem_end > bigger_right_now:
            bigger_right_now = elem_end
        else:
            right_bigger[j] = bigger_right_now

    water_vol = sum(
        max(min(left_bigger[i], right_bigger[i]) - arr[i], 0)
        for i in range(n))
    # for i in range(n):
    #     if left_bigger[i] and right_bigger[i]:
    #         water_vol += min(left_bigger[i], right_bigger[i]) - arr[i]

    return water_vol


if __name__ == "__main__":
    exs = [
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0],
        [1, 3, 2, 4, 1, 3, 1, 4, 5],
    ]
    for arr in exs:
        print(f"Water in {arr} is {get_lake_volumes(arr)}")
