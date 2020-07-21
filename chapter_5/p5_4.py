import utils.binutils as binutils

# TODO Handle the last bit correctly


def next_bigger(x: int) -> int:
    fugee_ones = x & 0b1
    temp = x >> 1
    flip_mask = binutils.ones(binutils.blen(x))
    bit_flip = 0b1 << 1
    flip_mask <<= 1

    # Find first non-trailing 0
    while (temp & 0b1 or not fugee_ones) and temp:
        bit_now = temp & 0b1
        fugee_ones += bit_now
        flip_mask <<= 1
        bit_flip <<= 1

        temp >>= 1
        # print(f"Looking at temp {temp:b}, bit_flip {bit_flip:b}")

    fugee_ones -= 1
    # print(f"Flip mask:\t{flip_mask:b}")
    # print(f"Bit flip:\t{bit_flip:b}")
    # print(f"Refugees:\t {fugee_ones}")

    # print(f"Original x:\t{x:b}")
    x &= flip_mask
    # print(f"Clearend x:\t{x:b}")
    x |= bit_flip  # Set target to 1
    # print(f"Bitfliped x:\t{x:b}")

    # Refugees to the right
    ref_mask = (0b1 << (fugee_ones)) - 1
    # print(f"Refugee mask is {ref_mask:b}")
    x |= ref_mask
    # print(f"Refmasked x:\t{x:b}\n" + "-" *50)
    return x

# 11_0_11111
# 11_1_00000
# 11_1_01111


def next_smaller(x: int) -> int:
    fugee_zeros = x & 0b1
    temp = x >> 1
    flip_mask = binutils.ones(binutils.blen(x))
    bit_flip = 0b1 << 1
    flip_mask <<= 1
    trailing_ones = True
    window_size = 0

    # Find first non-trailing 1
    while ((not temp & 0b1) or trailing_ones) and temp:
        bit_now = temp & 0b1

        fugee_zeros += not bit_now
        window_size += 1

        if not bit_now:
            trailing_ones = False

        flip_mask <<= 1
        bit_flip <<= 1

        temp >>= 1
        # print(f"Will look at temp {temp:b}, bit_flip {bit_flip:b}. {trailing_ones}")

    # print(f"Flip mask:\t{flip_mask:b}")
    # print(f"Bit flip:\t{bit_flip:b}")
    # print(f"Refugees:\t {fugee_zeros}")
    # print()
    # print(f"Original x:\t{x:b}")
    x &= flip_mask
    # print(f"Clearend x:\t{x:b}")

    flip_mask = binutils.ones(binutils.blen(x))
    flip_mask ^= bit_flip
    # print(f"Bitflip mask:\t{flip_mask:b}")

    x &= ~bit_flip  # 111_0_111, unset target bit
    # print(f"Bitfliped x:\t{x:b}")

    # Refugees to the left (make highest with available)
    ref_mask = (0b1 << (window_size - fugee_zeros + 1)) - 1
    ref_mask <<= fugee_zeros
    # print(f"Refugee mask is {ref_mask:b}")
    x |= ref_mask
    # print(f"Refmasked x:\t{x:b}\n" + "-" * 50)

    return x


if __name__ == "__main__":
    exs = [0b10011001, 0b10, 0b111000]
    for x in exs:
        print(f"For {x:b} < {next_bigger(x):b}\tand\t{x:b} > {next_smaller(x):b}")
