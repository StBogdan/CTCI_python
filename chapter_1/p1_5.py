
def is_edit(a: str, b: str) -> bool:
    la = len(a)
    lb = len(b)

    if la == lb:
        return check_subst(a, b)
    else:
        # Make a shorter
        if la > lb:
            a, b = b, a
        return check_edit(a, b)


def check_edit(a: str, b: str) -> bool:
    la = len(a)
    lb = len(b)
    i = 0
    j = 0
    mm = 0

    while i < la and j < lb:
        if a[i] == b[j]:
            i += 1
        else:
            mm += 1
        j += 1

        if mm > 1:
            return False

    return abs(i-j) <= 1


def check_subst(a, b) -> bool:
    mm = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            mm += 1
        if mm > 1:
            return False

    return True


if __name__ == "__main__":
    examples = [("pale", "ple"), ("pales", "pale"),
                ("pale", "bale"), ("pale", "bake"), ("babaqw", "babaw")]
    for a, b in examples:
        print(f"For {a} and {b} checking: {is_edit(a,b)}")
