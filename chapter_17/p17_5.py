# Method: Store seen letter/number balances (the first location)
# Time: O(n)
# Space: O(n)


def longest_subarr_number_letter_equal(arr: str) -> int:
    more_letters_now = 0
    seen_offsets = {0: -1}
    max_arr_size = 0
    max_arr_indexes = (-1, -1)

    for i in range(len(arr)):
        x = arr[i]

        if x.isdigit():
            more_letters_now -= 1
        else:
            more_letters_now += 1

        # print(f"Offsets: {seen_offsets}, letters more now: {more_letters_now}, elem now {x}")

        if more_letters_now in seen_offsets:
            max_arr_now = i - seen_offsets[more_letters_now]
            if max_arr_now > max_arr_size:
                max_arr_size = max_arr_now
                max_arr_indexes = (seen_offsets[more_letters_now] + 1, i)
        else:
            seen_offsets[more_letters_now] = i

    return max_arr_size, max_arr_indexes


if __name__ == "__main__":
    exs = ["aaa2222aa22aa222aaaa", "aaa222aa", "e4ee2a2a2a", "z0123456789a"]
    for ex_arr in exs:
        max_arr, (start, end) = longest_subarr_number_letter_equal(ex_arr)
        print(
            f"Max arr with eq is of len {max_arr}, "
            f"namely: {ex_arr[start:end+1]}, from {ex_arr}"
        )
