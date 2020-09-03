# idea: Reverse index

# create mapping from key: word , value: sorted set of occurences (count words in book)

# when looking for shortest distance between 2 words, run 2 pointers in the sorted arr, find min diff
import re
from typing import List
from collections import defaultdict
import os


def build_reverse_index(words: List[str]):
    rev_index = defaultdict(list)

    for index, word in enumerate(words):
        rev_index[word].append(index)

    return dict(rev_index)


def get_min_interword_distance(w1: str, w2: str, rev_index: dict):
    occ_w1 = rev_index[w1]
    occ_w2 = rev_index[w2]
    if not occ_w1 or not occ_w2:
        raise Exception("Not all words present")

    min_sum = float('inf')
    p1 = 0
    p2 = 0
    while p1 < len(occ_w1) and p2 < len(occ_w2):
        diff_now = abs(occ_w1[p1] - occ_w2[p2])
        if diff_now < min_sum:
            min_sum = diff_now

        if occ_w1[p1] > occ_w2[p2]:
            p2 += 1
        else:
            p1 += 1

    return min_sum


if __name__ == "__main__":
    with open(os.path.join("utils", "lorem_ipsum.txt")) as words_source:
        all_non_empty_words = filter(
            bool, re.split(" |\n|\.", words_source.read()))
        all_text = list(map(lambda x: x.lower(), all_non_empty_words))

    reverse_index = build_reverse_index(all_text)
    exs = [
        ("ultrices", "bibendum"),
        ("hendrerit", "nulla"),
    ]

    for w1, w2 in exs:
        print(f"Shortest distance b/t {w1} and {w2}"
              f" at {get_min_interword_distance(w1,w2, reverse_index)}")
