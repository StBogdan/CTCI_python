from typing import List


def find_duplicates(arr: List[int]) -> None:
    WORD_SIZE = 32  # Bytes
    bit_memory = [0b0] * 1000  # Assume 32 bit integers

    for x in arr:
        byte_target = x // WORD_SIZE
        inbyte_target = x % WORD_SIZE
        is_set = (bit_memory[byte_target] >> inbyte_target) & 0b1

        if is_set:
            print(x)
        else:
            bit_memory[byte_target] |= (0b1 << inbyte_target)


if __name__ == "__main__":
    arr = [31999, 1, 2, 7, 4, 5, 7, 30, 31999, 2, 2, 2, 1]
    find_duplicates(arr)
