# Method: Build new, counting occurences
# Time: O(n)
# Space: O(n)


def basic_compr(input_str: str) -> str:
    len_compres = 0
    len_orig = len(input_str)
    res = []

    prev = None
    prev_count = 0
    for c in input_str:
        if c != prev:
            if prev:
                res.append(prev)
                res.append(str(prev_count))
                len_compres += 1 + len(str(prev_count))
                if len_compres > len_orig:
                    return input_str
            prev = c
            prev_count = 1
        else:
            prev_count += 1

    res.append(prev)
    res.append(str(prev_count))

    len_compres += 1 + len(str(prev_count))

    return input_str if len_compres > len_orig else "".join(res)


if __name__ == "__main__":
    exs = ["aaaabbbb", "aaaaaaa", "abcdef", "abcdeeeeeeeeeee"]

    for ex in exs:
        print(f"String {ex} compresses in {basic_compr(ex)}")
