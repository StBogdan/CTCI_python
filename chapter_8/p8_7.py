import math

def perm_uniq(inp: str):
    return rec_perm("", inp)


def rec_perm(prefix, ltr_pool):
    if not ltr_pool:
        return [prefix]

    perms = []
    for i, ltr in enumerate(ltr_pool):
        nprefix = prefix + ltr
        sub_perm = rec_perm(nprefix, ltr_pool[:i] + ltr_pool[i+1:])
        perms += sub_perm

    return perms


if __name__ == "__main__":
    exs = ["a", "", "abc", "abcd", "abcdef"]

    for ex in exs:
        permutations = perm_uniq(ex)
        print(
            f"Perms {len(ex)} of nr {len(permutations)}"
            f" same as predicted {math.factorial(len(ex))}"
            f" \t{ex} are {permutations}")
