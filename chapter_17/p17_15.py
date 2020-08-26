from typing import List


def get_longest_gestaltwort(words: List[str]):
    known_words = {word: True for word in words}

    words_by_len = sorted(known_words, key=len, reverse=True)

    for word in words_by_len:
        for i in range(1, len(word)):
            if can_build_word(word, True, known_words):
                print(known_words)
                return word


def can_build_word(word, is_given_word, known_words):
    if word in known_words and is_given_word:
        return known_words[word]

    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]
        if left in known_words and known_words[left]\
                and can_build_word(right, False, known_words):
            known_words[word] = True
            return True

    known_words[word] = False
    return False


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
