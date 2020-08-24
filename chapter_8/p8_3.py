from typing import List


def find_magic_index(arr: List[int]) -> int:
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if mid == arr[mid]:
            return mid
        elif mid > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def find_magic_index_dups(arr: List[int]) -> int:
    return fmidh(arr, 0, len(arr)-1)


def fmidh(arr, s, e) -> int:
    if s > e:
        return -1

    mid = (s+e) // 2
    elem = arr[mid]

    if elem == mid:
        return mid

    lr = fmidh(arr, s, min(mid - 1, arr[mid]))
    if lr > 0:
        return lr

    rr = fmidh(arr, max(mid+1, arr[mid]), e)
    if rr > 0:
        return rr

    return -1


if __name__ == "__main__":
    ex1 = [-1, 1, 5, 6, 7, 8, 9, 10]
    ex_dups = [-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]

    print(f"A good index is {find_magic_index(ex1)}"
          f" same as {find_magic_index_dups(ex1)}, in {ex1}")
    print(f"With dups index: {find_magic_index_dups(ex_dups)} in {ex_dups}")
