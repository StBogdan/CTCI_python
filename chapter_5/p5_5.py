def is_power_of_two(n: int) -> bool:
    return (n & (n-1)) == 0


if __name__ == "__main__":
    exs = [0, 2, 4, 10, 23, 1, 64, 1024]
    for x in exs:
        print(f"Is {x} a power of two ? {is_power_of_two(x)}")
