from collections import defaultdict
from typing import List

def get_system_word_list(file_path="/usr/share/dict/words"):
    with open(file_path, "r") as system_words_file:
        big_list = list(map(lambda word: word.lower(),
                            system_words_file.read().split("\n")))
    return big_list

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
