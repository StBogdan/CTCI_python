from collections import defaultdict
from typing import List

# Wrong, but fun application of tries

def trie():
    return defaultdict(trie)


def build_trie_from_words(words: List[str]) -> dict:
    word_trie = trie()

    for word in words:
        current_pointer = word_trie
        for char in word:
            current_pointer = current_pointer[char]

        current_pointer["end"] = True

    return word_trie


def get_longest_gestaltwort(words: List[str]):
    word_trie = build_trie_from_words(words)

    c_max_len = 0
    c_max_word = 0

    for word in words:
        if is_composite(word, word_trie):
            if len(word) > c_max_len:
                c_max_len = len(word)
                c_max_word = word
    return c_max_word


def is_composite(word: str, word_trie: dict) -> bool:
    possible_split_pointers = []

    trie_pointer = word_trie
    for c in word:
        new_trie_pointer = trie_pointer[c]

        i = 0
        while i < len(possible_split_pointers):
            trie_pointer_subword = possible_split_pointers[i]
            if c not in trie_pointer_subword:
                possible_split_pointers.pop(i)
            else:
                possible_split_pointers[i] = trie_pointer_subword[c]
                i += 1

        if "end" in new_trie_pointer:
            possible_split_pointers.append(word_trie)

        # print(f"Char: {c} of {word}, current trie elems: {list(trie_pointer[c])},"
        #       f"\tpossible split pointers {[x.keys() for x in possible_split_pointers]}")
        trie_pointer = new_trie_pointer

    return any("end" in x for x in possible_split_pointers)


"""
for each word:
    check if partition exists
    for each char:
        if end of word in trie
            push to beginning
            add to possible split pointers

        for each of possible split pointes:
            advance to next letter if possible
            if not remove them from possible split pointers

for possible pointers:
    if any is at the end of a word, there is a valid partition
    record length against max
"""


def sys_word_test():
    with open("/usr/share/dict/words", "r") as system_words_file:
        big_list = list(map(lambda word: word.lower(),
                            system_words_file.read().split("\n")))

    print(f"Have a total of {len(big_list)} words")
    print(f"The longest is: {sorted(big_list, key = len)[-1]}")

    print(
        f"For the words, the longest is {get_longest_gestaltwort(big_list[1:])}")


if __name__ == "__main__":
    words = ["cat", "banana", "dog", "nana",
             "walk", "walker", "dogwalker", "catdognana"]
    print(f"For the words, the longest is {get_longest_gestaltwort(words)}")
