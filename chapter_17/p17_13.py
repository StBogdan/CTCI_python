from typing import List
from functools import lru_cache

# Method: DFS, prefix and best-of-rest with lookup against dict
# Time: O(n^2)
# Space: O(n)


def add_spaces(alltext: str, words: List[str]):
    word_set = set(words)
    space_arr, invalids = add_spaces_helper(alltext, 0, word_set, {})

    # print(f"Managed to do it with {invalids} characters unknown, splits {space_arr}")
    i = 0
    spaced_text = []
    for i in range(len(alltext)):
        spaced_text.append(alltext[i])
        if i in space_arr:
            spaced_text.append(" ")

    return "".join(spaced_text)


def add_spaces_helper(
    text: str,
    start_poz: int,
    word_set: set,
    memo: dict,
):
    if start_poz in memo:
        return memo[start_poz]

    n = len(text)
    if start_poz == n:
        return [], 0

    best_invals = n
    best_words = []

    left_side = ""
    for i in range(start_poz, n):
        left_side += text[i]

        invals = len(left_side) if left_side not in word_set else 0

        if invals < best_invals:

            rest_words, rest_invals_count = add_spaces_helper(
                text, i + 1, word_set, memo
            )

            if rest_invals_count + invals < best_invals:
                current_splits = [start_poz - 1, i] if invals == 0 else []
                best_invals = rest_invals_count + invals
                best_words = rest_words + current_splits

    # print(f"At start {start_poz} Got best words {best_words}, and invals {best_invals}")
    memo[start_poz] = (best_words, best_invals)

    return best_words, best_invals


if __name__ == "__main__":
    exs = ["helplinustechtipsineedtorebootmypc", "linusz", "torebootmy"]

    # words = utils.datasets.get_system_word_list()
    words = ["help", "tech", "tips", "boot", "my", "reboot", "need", "to", "linus"]
    for ex in exs:
        print(f"The way to split '{ex}' is: '{add_spaces(ex, words)}'")
