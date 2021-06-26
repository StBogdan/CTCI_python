from collections import defaultdict
from typing import List

# Method: Create a suffix tree, lookup each word against it
# Time: O(b^2 + w * b)
# Space: O(b^2)
# Note: w = words


def find_in_string(bigstr: str, words: List[str]):
    sufix_trie = create_suffix_trie(bigstr)
    res_dict = {}

    for word in words:
        pozs = find_starts(sufix_trie, word)
        res_dict[word] = pozs

    return res_dict


def find_starts(trie: dict, word: str) -> List[int]:
    trie_pointer = trie
    for c in word:
        if c not in trie_pointer:
            return []
        else:
            trie_pointer = trie_pointer[c]

    return [end_index - len(word) + 1 for end_index in trie_pointer["index"]]


def build_trie_from_words(words: List[str]) -> dict:
    word_trie = trie()

    for word in words:
        add_word_to_trie(word)

    return word_trie


def trie():
    return defaultdict(trie)


def create_suffix_trie(word):
    sufs_trie = trie()
    suffix_now = word
    start_index = 0

    while suffix_now:
        add_word_to_trie(sufs_trie, suffix_now, start_index)
        suffix_now = suffix_now[1:]
        start_index += 1

    return sufs_trie


def add_word_to_trie(trie: dict, word: str, start_index=0) -> None:
    current_pointer = trie
    index_of_chr = start_index
    for char in word:
        current_pointer = current_pointer[char]
        if "index" in current_pointer:
            current_pointer["index"].append(index_of_chr)
        else:
            current_pointer["index"] = [index_of_chr]
        index_of_chr += 1

    current_pointer["end"] = True


if __name__ == "__main__":
    exs = [("mississippi", ["i", "iss", "ppi", "miss", "issi", "ipi"])]
    for bigword, targets in exs:
        print(f"{[x for x in range(len(bigword))]}")
        print(" " + ", ".join(bigword))
        print(f"Found targets at {find_in_string(bigword, targets)}")
