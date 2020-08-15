# Binary utilities

def blen(a: int):
    return len(bin(a)) - 2


def ones(number: int):
    return (0b1 << (number)) - 1


if __name__ == "__main__":
    print(f"{ones(5):b}")
