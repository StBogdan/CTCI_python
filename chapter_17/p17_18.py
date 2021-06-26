from typing import List
from collections import defaultdict

# Method: Two pointer, keep track of elements
# Time: O(l)
# Space: O(s)


def longest_superseq(longer: List[int], shorter: List[int]) -> List[int]:
    short_set = set(shorter)
    count_now = defaultdict(int)

    start = 0
    number_uniq = 0

    min_seq_now = float("inf")
    min_seq_indexes = (-1, -1)

    for i in range(len(longer)):
        x = longer[i]
        if x in short_set:
            if count_now[x] == 0:
                number_uniq += 1
            count_now[x] += 1

        while number_uniq == len(shorter) and start < i:
            current_subseq_len = i - start + 1
            if current_subseq_len < min_seq_now:
                min_seq_now = current_subseq_len
                min_seq_indexes = (start, i)

            if longer[start] in short_set:
                count_now[longer[start]] -= 1

                if count_now[longer[start]] == 0:
                    number_uniq -= 1

            start += 1

    return list(min_seq_indexes)


if __name__ == "__main__":
    exs = [
        ([1, 5, 9], [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]),
        ([1, 2, 3], [1, 1, 2, 2, 2, 3, 3, 9, 9, 2, 1, 1, 3]),
    ]

    for shorter, longer in exs:
        print(
            f"Between {longest_superseq(longer,shorter)}, "
            f"you will find {shorter} in {longer}"
        )
