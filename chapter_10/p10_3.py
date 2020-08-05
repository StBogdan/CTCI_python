def search_rot_arr(arr_rotated, num):
    n = len(arr_rotated)

    if not arr_rotated:
        return -1
    elif n == 1:
        return 0 if arr_rotated[0] == num else -1
    elif arr_rotated[0] < arr_rotated[-1]:
        return binary_search(arr_rotated, 0, n-1, num)

    pivot_index = find_pivot_index(arr_rotated)
    res_index = -1

    print(f"Found pivot index: {pivot_index}")

    search_start, search_end = \
        (pivot_index+1, n-1) if num <= arr_rotated[-1] else (0, pivot_index)
    return binary_search(arr_rotated, search_start, search_end, num)


def binary_search(arr, s, e, target):
    low = s
    high = e
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1

    return -1


def find_pivot_index(arr):
    """Addresable index of the last element before pivot"""
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high) // 2  # Divide and floor

        if mid == len(arr):
            return 0

        if arr[mid+1] < arr[mid]:
            return mid

        if arr[mid] > arr[-1]:
            low = mid+1
        else:
            high = mid - 1

    return 0


if __name__ == "__main__":
    exs = [([2], 2),
           ([1, 2], 2),
           ([0, 1, 2, 3, 4, 5], 1),
           ([9, 12, 17, 2, 4, 5], 17),
           ([9, 12, 17, 2, 4, 5, 6], 4)]
    for arr, target in exs:
        print(
            f"Looking for {target} in {arr}, found location ? {search_rot_arr(arr, target)}")
