# Method: Attach to itself
# Time: O(n) (create new string, potentially substring check)
# Space: O(n) (store the new big string)


def checkrot(s1: str, s2: str):
    s22 = s2 + s2
    return isSubstr(s1, s22) and len(s1) == len(s2)


def isSubstr(s1: str, s2: str) -> bool:
    return s1 in s2


if __name__ == "__main__":
    ex1 = ("abc", "cab")
    ex2 = ("panama", "ampaan")
    ex3 = ("ab", "abc")

    for a, b in (ex1, ex2, ex3):
        print(f"Is {a} rot of {b} ? {checkrot(a,b)}")
