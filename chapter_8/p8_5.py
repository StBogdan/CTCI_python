from functools import lru_cache


def rec_mult(a: int, b: int) -> int:
    if not a or not b:
        return 0
    sm, bg = (a, b) if a < b else (b, a)
    return rmh(sm, bg)


@lru_cache(None)
def rmh(sm, bg):
    if sm == 1:
        return bg

    prod = rmh(sm//2, bg)
    prod += prod
    if sm % 2:
        prod += bg

    return prod


if __name__ == "__main__":
    exs = [(0, 1), (1, 0), (3, 3), (9, 9), (50, 50), (5, 7)]
    for a, b in exs:
        print(f"{a} times {b} is {a*b} same as {rec_mult(a,b)}")
