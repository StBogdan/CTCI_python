def flips_to_convert(a: int, b: int) -> int:
    flip_c = 0
    while a and b:
        flip_c += (a & 0b1) ^ (b & 0b1)
        a >>= 1
        b >>= 1

    while a:
        flip_c += a & 0b1
        a >>= 1
    while b:
        flip_c += b & 0b1
        b >>= 1

    return flip_c


if __name__ == "__main__":
    exs = [(0b1000010101, 0b1111), (0b11101, 0b01111),
           (0b1, 0b101), (0b101, 0b101)]
    for a, b in exs:
        print(f"Converting {a:b} into {b:b} flips {flips_to_convert(a,b)}")
