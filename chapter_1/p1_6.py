def basic_compr(a: str) -> str:
    cl = 0
    n = len(a)
    res = []

    prev = None
    prev_count = 0
    for c in a:
        if c != prev:
            if prev:
                res.append(prev)
                res.append(str(prev_count))
                cl += 1 + len(str(prev_count))
                if cl > n:
                    return a
            prev = c
            prev_count = 1
        else:
            prev_count += 1

    res.append(prev)
    res.append(str(prev_count))

    cl += 1 + len(str(prev_count))

    return a if cl > n else "".join(res)


if __name__ == "__main__":
    exs = ["aaaabbbb", "aaaaaaa", "abcdef", "abcdeeeeeeeeeee"]

    for ex in exs:
        print(f"String {ex} compresses in {basic_compr(ex)}")
