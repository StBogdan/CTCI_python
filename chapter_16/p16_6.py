def binary_search_around(arr, target):
    low = 0
    high = len(arr)-1

    mid = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return (mid, mid)
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid+1

    lower = None
    higher = None
    if arr[mid] > target:
        higher = mid
        if mid > 0:
            lower = mid-1
    else:
        lower = mid
        if lower < len(arr)-1:
            higher = mid+1

    return (lower, higher)


def smallest_diff(arr1, arr2) -> int:
    cmin_diff = float("inf")
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    sorted_arr = sorted(arr1)
    for x in arr2:
        smaller, bigger = binary_search_around(sorted_arr, x)
        print(f"For x {x} got around elems: {smaller} and {bigger}")

        diff_with_bigger = sorted_arr[bigger] - x \
            if bigger is not None else float('inf')
        diff_with_smaller = x - sorted_arr[smaller] \
            if smaller is not None else float('inf')

        diff_now = min(diff_with_bigger, diff_with_smaller)
        if diff_now < cmin_diff:
            cmin_diff = diff_now

    return cmin_diff


if __name__ == "__main__":
    exs = [
        ([1], [23, 127, 235, 19, 8])
    ]

    for arr1, arr2 in exs:
        print(f"Minimum is {smallest_diff(arr1,arr2)}"
              f" for the arrays {arr1} and {arr2}")
