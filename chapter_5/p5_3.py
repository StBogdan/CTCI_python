def longest_seq_by_flip(x: int) -> int:
    max_join = -1
    seq_prev = 0
    seq_now = 0

    zeros_in_str = False
    prev_was_zero = False
    joinable_gap = False

    while x:
        bit_now = x & 0b1
        x >>= 1
        if bit_now:
            prev_was_zero = False
            seq_now += 1
        else:
            zeros_in_str = True
            if joinable_gap and seq_now != 0:
                if seq_now + seq_prev + 1 > max_join:
                    max_join = seq_now + seq_prev + 1

            if seq_now > 0:
                # If there is a seq and a 0, check if len(that)+1 is largest
                if seq_now + 1 > max_join:
                    max_join = seq_now+1
                # Update for next seq
                seq_prev = seq_now
                seq_now = 0

            joinable_gap = not prev_was_zero
            prev_was_zero = True

        # print(f"At bit {bit_now},\tseq_now: {seq_now},\tseq_prev: {seq_prev},\tjoin_gap {joinable_gap},\tprev_was_zero {prev_was_zero}")

    if joinable_gap:
        if seq_now + seq_prev + 1 > max_join:
            max_join = seq_now + seq_prev + 1
    elif seq_now + zeros_in_str > max_join:
        # Cover the case of all ones, or one seq with trailing zeros
        max_join = seq_now + zeros_in_str

    return max_join


if __name__ == "__main__":
    exs = [(0b111, 3), (0b101, 3), (0b111001, 4), (0b1010101, 3),
           (0b1011, 4), (0b101100, 4), (0b110, 3), (0b100111001, 4)]
    for ex, target in exs:
        print(
            f"Biggest seq for {ex:b} is {longest_seq_by_flip(ex)} == {target}")
