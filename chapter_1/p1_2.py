from collections import Counter

# Method: Sort and compare
# Time: O(n*log(n))
# Space: O(n)


def check_perm(a: str, b: str):
    sa = sorted(a)
    sb = sorted(b)

    return sb == sa


def check_perm_ctr(a: str, b: str):
    ca = Counter(a)
    cb = Counter(b)

    for k, v in ca.items():
        if k not in cb:
            return False
        elif v != cb[k]:
            return False

    if any(k not in ca for k in cb):
        return False

    return True


if __name__ == "__main__":
    inputs = [("aa", "ac"), ("", ""), ("saodk", "dkoas"), ("cab", "baac")]

    for a, b in inputs:
        print(
            f"Bot input {a} and {b}, result {check_perm(a,b)}"
            f" == {check_perm_ctr(a,b)}")
