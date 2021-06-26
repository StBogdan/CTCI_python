from typing import List

# Method: If there is a majority element, it's going to have enough buget to displace all others
# Time: O(n)
# Space: O(1)


def majority_elem(arr):
    candidate = maj_elem(arr)
    return candidate if is_majority(candidate, arr) else -1


def is_majority(x: int, arr: List[int]) -> bool:
    count = 0
    for elem in arr:
        count += elem == x
    print(f"Count is {count}")
    return count > len(arr) / 2


def maj_elem(arr: List[int]) -> int:
    elem_now = arr[1]
    count = 1
    for i in range(1, len(arr)):
        x = arr[i]
        if x == elem_now:
            count += 1
        else:
            count -= 1

        if count < 1:
            elem_now = x
            count = 1
    return elem_now


if __name__ == "__main__":
    posib = [4, 4, 4, 4, 5, 5, 5, 5, 5]
    print(majority_elem(posib))
