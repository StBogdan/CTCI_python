import string
from collections import Counter

# Method: Map and check for odds
# Time: O(n)
# Space: O(n)

# Method: Character bit-map, check set bits
# Time: O(n)
# Space: O(1) (limited by alphabet)


def is_palindrom_perm(word: str) -> bool:
    clean_w = pre_process(word)
    ctr = Counter(clean_w)
    odd_c = sum(x % 2 for x in ctr.values())
    return not odd_c > 1


def is_palindrome_perm_better(word: str) -> bool:
    bs = {c: 0b0 for c in string.ascii_lowercase}
    for c in pre_process(word):
        bs[c] ^= 0b1  # Flip by xor with one
    return not sum(x for x in bs.values()) > 1


def pre_process(x: str) -> str:
    # x.translate(string.maketrans("","",string.punctuation))
    letter_iter = filter(lambda c: c.isalpha(), x.strip())
    return "".join(map(lambda x: x.lower(), letter_iter))


if __name__ == "__main__":
    print(pre_process("a...!>!>!a<<>  <!!!aaa"))

    def printex(ex): return print(
        f"For exampple: {ex} ==> {is_palindrom_perm(ex)} \
        same as {is_palindrome_perm_better(ex)}")

    ex1 = "A man, a plan, a canal, panama"
    printex(ex1)
    ex2 = "This is not a plaindrome"
    printex(ex2)
    ex3 = "aaaaccbbb"
    printex(ex3)
