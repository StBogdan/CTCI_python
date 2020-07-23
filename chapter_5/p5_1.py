from utils.binutils import blen


def binary_insert(n: int, m: int, i: int, j: int) -> int:
    len_n = blen(n)
    len_m = blen(m)

    mask = 0b1 << (len_n - j - 1)
    mask -= 1
    # print(f"Mask is\t{mask:b}")

    mask <<= j + 1
    # print(f"Mask is\t{mask:b}")

    mask += (0b1 << i+1) - 1
    # print(f"Mask is\t{mask:b}")
    # print(f"N is\t{n:b}")
    n &= mask
    print(f"N is\t{n:b}")

    j_mask = m << i
    # print(f"Jmask is\t{j_mask:b}")
    n |= j_mask
    return n


if __name__ == "__main__":
    n = 0b11110000001
    m = 0b1111
    i = 2
    j = 6

    print(f"Result of insertion is: {bin(binary_insert(n,m,i,j))}")
