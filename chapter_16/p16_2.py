from collections import defaultdict
from typing import List
import string


def word_freq_setup(words: List[str]):
    ctr = defaultdict(lambda: 0)
    for word in words:
        proc_word = word.strip().lower().translate(
            str.maketrans('', '', string.punctuation))
        if not proc_word:
            continue
        ctr[proc_word] += 1
    return ctr


def lookup_word(word: str, words_counts: dict) -> int:
    proc_word = word.strip() \
                    .lower() \
        .translate(str.maketrans('', '', string.punctuation))
    if proc_word in words_counts:
        return words_counts[proc_word]
    else:
        raise Exception(f"Word \"{proc_word}\" not found")


if __name__ == "__main__":
    big_text = """The missile knows where it is at all times. 
    It knows this because it knows where it isn't. 
    By subtracting where it is from where it isn't, or where it isn't from where it is (whichever is greater), it obtains a difference, or deviation. 
    The guidance subsystem uses deviations to generate corrective commands to drive the missile from a position where it is to a position where it isn't, and arriving at a position where it wasn't, it now is. 
    Consequently, the position where it is, is now the position that it wasn't, and it follows that the position that it was, is now the position that it isn't.
    In the event that the position that it is in is not the position that it wasn't, the system has acquired a variation, the variation being the difference between where the missile is, and where it wasn't. 
    If variation is considered to be a significant factor, it too may be corrected by the GEA. However, the missile must also know where it was.
    The missile guidance computer scenario works as follows. 
    Because a variation has modified some of the information the missile has obtained, it is not sure just where it is. 
    However, it is sure where it isn't, within reason, and it knows where it was. 
    It now subtracts where it should be from where it wasn't, or vice-versa, and by differentiating this from the algebraic sum of where it shouldn't be, and where it was, it is able to obtain the deviation and its variation, which is called error."
    """
    lookup_list = "missile", "it", "It", "was", "wasn't", "the", "tHE"

    word_dict = word_freq_setup(big_text.split(" "))
    for word in lookup_list:
        try:
            print(f"Found word: {word} {lookup_word(word, word_dict)}")
        except Exception as e:
            print(f"Didn't find {word} in dict")
