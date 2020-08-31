
from typing import List, Tuple
from copy import copy
import utils.datasets
from collections import defaultdict


# For each word size, starting with the largest
#  Get list of words of that lenght
#  Try all combos
        # Place one
        # For each letter, have a big trie traversal pointer
        # Check that there is at least one word with those letters (of the current to add, and the previous letters)
        # Also see which ones end (If all, add as candidate)
        # Add another 


def word_square_helper(all_words_trie:dict,
        words_of_len: set,
        used_words: List[str],
        current_trie_pointers: List[dict]):

    current_best = None
    for word in words_of_len - set(used_words):
        stack_score, new_trie_pointers = get_stack_score(all_words_trie, current_trie_pointers, word)  

        if stack_score ==  -1:
            continue
        
        # print(f"For words used {used_words} and {word:20}, got stack score: {stack_score}")

        if stack_score == len(word):
            # print(f"Got a good one at {used_words} and {word}")
            current_best = used_words + [word]

        best_of_rest = word_square_helper(all_words_trie, words_of_len, used_words + [word], new_trie_pointers)
        if best_of_rest:
            current_best = best_of_rest
    
    return current_best

def get_stack_score(big_trie, trie_pointer_list, new_word) -> Tuple[int, list]:
    new_trie_pointers = copy(trie_pointer_list)
    words_that_end_here = 0
    for i in range(len(new_word)):
        trie_ptr = new_trie_pointers[i]
        char_now = new_word[i]

        if char_now not in trie_ptr:
            return -1, None
        
        new_trie_pointers[i]= trie_ptr[char_now]
        if "end" in new_trie_pointers[i]:
            words_that_end_here+=1
    
    return words_that_end_here, new_trie_pointers

def get_largest_word_matrix(word_list: List[str]) -> List[str]:
    words_by_len = defaultdict(set)

    max_word_len = len(max(word_list, key=len))
    for word in word_list:
        words_by_len[len(word)].add(word)

    big_word_trie = utils.datasets.build_trie_from_words(word_list)

    best_total_chars = 0
    best_total_square = None

    for i in range(max_word_len, 0, -1):
        print(f"Checking words of len {i}, about {len(words_by_len[i])} of them")
        best_of_len = word_square_helper(big_word_trie, words_by_len[i], [], [big_word_trie]*i)
        total_chars = len(best_of_len) * i if best_of_len else 0

        if total_chars > best_total_chars:
            best_total_chars = total_chars
            best_total_square = best_of_len
    
    return best_total_square


if __name__ == "__main__":
    big_word_list = utils.datasets.get_system_word_list()
    big_word_list = list(filter(lambda x: 6 > len(x) > 2, big_word_list))

    result =  get_largest_word_matrix(big_word_list)
    for word in result:
        print("".join(c + " " for c in word) + f" in worlist? {word in big_word_list}")

    for i in range(len(result[0])):
        colword= "".join(result[j][i] for j in range(len(result)))

        print(f"Colword {colword} in wordlist ? {colword in big_word_list}")
    


        



















