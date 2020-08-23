def zeroes_in_fact(n: int):
    five_pow = 1
    nr_z = 0
    while (5**five_pow) <= n:
        nr_z += (n // 5 ** five_pow)
        five_pow += 1
    return nr_z


if __name__ == "__main__":
    exs = [1, 10, 34, 55, 642, 1000]
    for ex in exs:
        print(f"Number of zeroes in {ex}! is {zeroes_in_fact(ex)}")
