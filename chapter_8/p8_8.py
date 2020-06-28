from collections import Counter
from typing import List
import math


def perm_dups(words: str):
    count = Counter(words)
    res_list_list = perm_w_count(count)
    return ["".join(res) for res in res_list_list]


def perm_w_count(counter: dict) -> List[List]:
    res = []
    has_to_place = False

    for k, v in counter.items():
        if v > 0:
            has_to_place = True
            call_dict = counter.copy()
            # print(f"Call dict is {call_dict}")
            call_dict[k] -= 1
            res_subcall = perm_w_count(call_dict)
            res.extend([[k] + rest for rest in res_subcall])

    if not has_to_place:
        return [[""]]
    else:
        return res


if __name__ == "__main__":
    exs = ["a", "", "abc", "abcd", "aaab", "bbaa", "calalc", "aqa"]

    for ex in exs:
        permutations = perm_dups(ex)
        print(
            f"Perms input len: {len(ex)} of computed: {len(permutations)}"
            f" \t{ex} are {permutations}")
        print("-"*50)
