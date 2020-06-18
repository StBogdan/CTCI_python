import string
from collections import Counter


def is_palindrom_perm(word: str) -> bool:
    clean_w = proc(word)
    ctr = Counter(clean_w)
    odd_c = sum(x % 2 for x in ctr.values())
    return not odd_c > 1


def is_palindrome_perm_better(word: str) -> bool:
    bs = {c: 0b0 for c in string.ascii_lowercase}
    for c in proc(word):
        bs[c] ^= 0b1  # Flip by xor with one
    return not sum(x for x in bs.values()) > 1


def proc(x: str) -> str:
    # x.translate(string.maketrans("","",string.punctuation))
    letter_iter = filter(lambda c: c.isalpha(), x.strip())
    return "".join(map(lambda x: x.lower(), letter_iter))


if __name__ == "__main__":
    print(proc("a...!>!>!a<<>  <!!!aaa"))

    def printex(ex): return print(
        f"For exampple: {ex} ==> {is_palindrom_perm(ex)} \
        same as {is_palindrome_perm_better(ex)}")

    ex1 = "A man, a plan, a canal, panama"
    printex(ex1)
    ex2 = "This is not a plaindrome"
    printex(ex2)
    ex3 = "aaaaccbbb"
    printex(ex3)
