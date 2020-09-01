from typing import List, Iterable
from collections import defaultdict
import utils.datasets


T9_MAP = {
    0: set(),
    1: set(),
    2: {'a', 'b', 'c'},
    3: {'d', 'e', 'f'},
    4: {'g', 'h', 'i'},
    5: {'j', 'k', 'l'},
    6: {'m', 'n', 'o'},
    7: {'p', 'q', 'r', 's'},
    8: {'t', 'u', 'v'},
    9: {'w', 'x', 'y', 'z'}
}


def rec_def_dict():
    return defaultdict(rec_def_dict)


def create_trie_from_words(words: Iterable[str]):
    trie_root = rec_def_dict()
    for word in words:
        trie_pointer = trie_root
        for char in word:
            trie_pointer = trie_pointer[char]

        trie_pointer["end"] = word

    return trie_root


def t9_trav_helper(digits: List[int], offset: int, pointer: dict) -> List[str]:
    if offset == len(digits):
        if "end" in pointer:
            return [pointer["end"]]
    else:
        letters = T9_MAP[digits[offset]]
        words = []

        for c in letters:
            if c in pointer:
                new_pointer = pointer[c]
                new_words = t9_trav_helper(digits, offset + 1, new_pointer)
                if new_words:
                    words += new_words

        return words


def get_t9_words(input_digits: str, words: List[str]) -> List[str]:
    trie_root = create_trie_from_words(words)
    digit_list = list(map(int, input_digits))
    return t9_trav_helper(digit_list, 0, trie_root)


if __name__ == "__main__":
    sys_word_list = list(map(lambda x: x.lower(),
                             utils.datasets.get_system_word_list()))
    exs = [
        "8733",
        "2222",
        "798466",
        "32573"
    ]
    for ex in exs:
        print(f"For input {ex}, possible words are: "
              f"{get_t9_words(ex, sys_word_list)}")
