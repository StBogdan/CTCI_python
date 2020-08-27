from typing import List, Tuple


def get_left_sorted(arr):
    # Find left side, returns first index after
    left_max, end_left = arr[0], 0

    while end_left < len(arr) and arr[end_left] >= left_max:
        left_max = arr[end_left]
        end_left += 1
    # print(f"End left is {end_left}, {arr[:end_left+1]}")
    return end_left


def get_right_sorted(arr):
    # Find right side
    start_right = len(arr)-1
    right_min = arr[-1]
    while start_right > 0 and arr[start_right] <= right_min:
        right_min = arr[start_right]
        start_right -= 1
    # print(f"Start right is {start_right} , {arr[start_right:]}")
    return start_right


def find_sub_sort(arr: List[int]) -> Tuple[int, int]:
    # arr is: left | middle | right
    n = len(arr)

    end_left = get_left_sorted(arr)
    start_right = get_right_sorted(arr)

    if end_left == n:  # Array already sorted
        return (0, 0)

    # Calc middle
    mid_min = float("inf")
    mid_max = -float("inf")

    for i in range(end_left, start_right+1):
        mid_min = min(mid_min, arr[i])
        mid_max = max(mid_max, arr[i])
    # print(
    #     f"For the mid section {arr[end_left:start_right+1]},"
    #     f" min {mid_min}, max {mid_max}")

    # Expand middle leftwards
    while end_left > 0 and arr[end_left-1] > mid_min:
        end_left -= 1
    # print(f"Expanded left now to: {end_left}")

    # Expand middle rightwards
    while start_right < n-1 and arr[start_right+1] < mid_max:
        start_right += 1
    # print(f"Expanded right now to: {start_right}")

    return (end_left, start_right)


if __name__ == "__main__":
    exs = [
        [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19],
        [1, 2, 3, 4, 5],
        [7, 12, 3, 4, 5, 6, 0]
    ]
    for arr in exs:
        print(
            f"To sort {arr}, we need to sort sub arr between {find_sub_sort(arr)} ")
