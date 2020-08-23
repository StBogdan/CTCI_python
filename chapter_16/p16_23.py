import random
from collections import defaultdict

STATISTICAL_SIGNIF_THRESHOLD = 10**6


def rand5() -> int:
    return random.randint(0, 4)


def rand7() -> int:
    res = rand5()*5 + rand5()  # Get res in range 0-24
    while res >= 21:  # Reroll until in 7-divisible range
        res = rand5()*5 + rand5()

    return res % 7


if __name__ == "__main__":
    results = defaultdict(lambda: 0)
    for _ in range(STATISTICAL_SIGNIF_THRESHOLD):
        results[rand7()] += 1

    for x in sorted(results.keys()):
        print(f"Value {x} found times: {results[x]}")
