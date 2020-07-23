def pairwise_swap(a: int) -> int:
    select_mask = 0xAAAAAAAA  # 16 A's
    odd_bits = a & select_mask
    even_bits = (a << 1) & select_mask
    return (odd_bits >> 1) | (even_bits)


if __name__ == "__main__":
    exs = [0b1010, 0b1111, 0b100, 0b110, 0b100101]
    for x in exs:
        print(f"Swapping {x:10b} --> {pairwise_swap(x):10b}")
