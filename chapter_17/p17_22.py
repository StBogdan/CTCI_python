from typing import List
from collections import deque
import utils.datasets


def wildcard_match(w1: str, w2: str, wildcard_index: int) -> bool:
    for i in range(len(w1)):
        if i == wildcard_index:
            continue
        elif w1[i] != w2[i]:
            return False
    return True


def get_one_related_words(word: str, word_set: set, used_words: set):
    related_words = set()
    available_words = word_set - used_words
    for i in range(len(word)):
        related_words.update(
            filter(lambda new_word: wildcard_match(word, new_word, i),
                   available_words))

    return related_words


def word_transf(w1: str, w2: str, words: List[str]) -> List[str]:
    if len(w1) != len(w2):
        return []

    word_set = set(word for word in words if len(word) == len(w1))
    queue = deque()
    queue.append((w1, []))
    seen = {w1}

    while queue:
        elem_now, path_to_here = queue.popleft()
        seen.add(elem_now)

        if elem_now == w2:
            return path_to_here + [w2]

        children = get_one_related_words(elem_now, word_set, seen)
        for child_word in children:
            if child_word not in seen:
                seen.add(child_word)
                queue.append((child_word, path_to_here + [elem_now]))

    return []


if __name__ == "__main__":
    all_words = utils.datasets.get_system_word_list()
    exs = [
        ("damp", "like"),
        ("dank", "gene")
    ]
    for a, b in exs:
        print(f"Way from '{a}' to '{b}' is via {'->'.join(word_transf(a,b, all_words))}")
