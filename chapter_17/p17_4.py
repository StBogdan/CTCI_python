from typing import List

# Method: Count expected evens and odds, tehnically O(log_2(n^2))
# Time: O(n)
# Space: O(n)


def get_bit(a: int, bit_nr: int) -> int:
    shifted_a = a >> (bit_nr)
    return shifted_a & 0b1


def find_mssing(arr: List[int], n: int) -> int:
    return find_missing_helper(arr, list(range(len(arr))), 0, n)


def find_missing_helper(
    arr: List[int], list_indexes: List[int], bit_offset: int, n: int
) -> int:
    if n == 0:
        return 0

    odds = []
    evens = []
    for i in list_indexes:
        bit_now = get_bit(arr[i], bit_offset)
        if bit_now:
            odds.append(i)
        else:
            evens.append(i)

    expected_odds = 0
    expected_evens = 0
    for i in range(n + 1):
        if i & 0b1:
            expected_odds += 1
        else:
            expected_evens += 1

    if len(evens) < expected_evens:
        bit_now = 0
        rest = find_missing_helper(arr, evens, bit_offset + 1, n >> 1)
    else:
        bit_now = 1
        rest = find_missing_helper(arr, odds, bit_offset + 1, n >> 1)

    # print(f"Bit now is {bit_now}, rest {rest},"
    #       f" evens: {evens} (expected {expected_evens}),"
    #       f" odds: {odds} (expected {expected_odds})")
    return (rest << 1) | bit_now


if __name__ == "__main__":
    exs = [
        ([0, 1, 2], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8], 8),
        ([0, 1, 2, 3, 5], 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 0], 9),
    ]

    for arr, n in exs:
        print(f"In arr {arr}, with limit {n}, missing is {find_mssing(arr,n)}")
