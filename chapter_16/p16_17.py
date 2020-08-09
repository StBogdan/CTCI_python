from typing import List


def largest_sum_cseq(arr: List[int]):
    max_now = 0
    sum_now = 0

    for x in arr:
        sum_now += x
        if sum_now > max_now:
            max_now = sum_now

        if sum_now < 0:
            sum_now = 0

    return max_now


if __name__ == "__main__":
    exs = [([2, -8, 3, -2, 4, -10], 5),
           ([1, 2, 3, 4, 5, 6], 21),
           ([-10, 100, -5, -5, -5, -5, -5, 1, 2, 3, 4, 25, -50], 110)]

    for arr, target in exs:
        print(f"Largest sum in {arr} is {largest_sum_cseq(arr)},"
              f" expected {target}")
