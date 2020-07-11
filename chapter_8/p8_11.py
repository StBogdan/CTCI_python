from typing import List


def repr_w_coints(cents: int) -> int:
    coins = [25, 10, 5, 1]
    return coin_repr(cents, 0, coins)


def coin_repr(n: int, start_ci: int, coins: List[int]) -> int:
    ways = 0
    if n < 0:
        return 0
    if n == 0:
        return 1

    for i in range(start_ci, len(coins)):
        ways += coin_repr(n-coins[i], i, coins)

    return ways


if __name__ == '__main__':
    exs = [1, 3, 4, 10, 20, 30, 40, 50, 60]
    for ex in exs:
        print(f"Way to repr {ex} is {repr_w_coints(ex)}")
