from typing import List


def sum_swap(arr1: List[int], arr2: List[int]) -> tuple:
    if len(arr1) < len(arr2):
        return sum_swap(arr2, arr1)

    posibs_set = set(arr2)
    target_change = abs(sum(arr1) - sum(arr2))

    if target_change % 2 == 1:
        return None
        target_change //= 2

    for x in arr1:
        if x-target_change in posibs_set:
            return (x, x-target_change)
        elif x+target_change in posibs_set:
            return (x, x + target_change)

    return None


if __name__ == "__main__":
    exs = [
        ([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 4])
    ]

    for arr1, arr2 in exs:
        print(f"Swap {sum_swap(arr1, arr2)} to make {arr1} have same sum ar {arr2}")
