from typing import List


def sparse_search(warr: List[str], target):
    low = 0
    high = len(warr) - 1
    while low <= high:
        mid = (low + high) // 2

        # Go right until limit or non-empty
        while mid < high and not warr[mid]:
            mid += 1

        if warr[mid] == target:
            return mid
        elif (not warr[mid]) or warr[mid] > target:
            # In case that right side is empty, look left
            high = mid-1
        else:
            low = mid+1
    return -1


if __name__ == "__main__":
    test_arr = ['b', '', '', 'car', '', '', 'tar', '', '', '', '', 'zar']
    exs = [(test_arr, 'zar'),
           (test_arr, 'car'),
           (test_arr, "potato"),
           (test_arr, 'b'),
           ([''], "potato"),
           (['', 'aaa', ''], 'aaa'),
           (['aaa'], 'aaa')]
    for arr, target in exs:
        print(f"Position of {target}\tis {sparse_search(arr,target)}\tin {arr}")
