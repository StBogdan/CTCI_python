
# Method: Bitwise addition, recurse with carry
# Time: O(log(n))
# Space: O(log(n))

def add_overfill(left, res, ctr, carry):
    while left:
        # print(f"Diggin into {left:b}, resutl now {res:b}")
        res_bit = left & 1

        if carry:
            carry = res_bit & carry
            res_bit ^= 0b1
        else:
            carry = res_bit & carry

        res ^= raise_to_counter(res_bit, ctr)

        ctr <<= 1
        ctr ^= 1

        left >>= 1
    return res, ctr, carry


def raise_to_counter(a_bit, ctr):
    ctemp = ctr
    while ctemp:
        a_bit <<= 1
        ctemp >>= 1
    return a_bit


def add_no_alg(a, b):

    res = 0b0
    ctr = 0b0
    carry = 0b0

    while a and b:
        bit_b = b & 1
        bit_a = a & 1
        res_b = bit_a ^ bit_b
        # print(f"Adding {bit_a:b} & {bit_b:b} => {res_b:b}, incoming carry: {carry:b}")

        if carry:
            if bit_a & bit_b:
                carry = 0b1
            else:
                carry &= res_b
            res_b ^= 0b1
            # print(f"Added carry, now result {res_b:b}, further carry {carry:b}")
        else:
            carry = bit_a & bit_b
            # print(f"Carry set to {carry}")

        res ^= raise_to_counter(res_b, ctr)
        # print(f"Res_b is {res_b:b}, carry {carry:b}, counter is {ctr:b}")

        ctr <<= 1
        ctr ^= 1

        a >>= 1
        b >>= 1
        # print( f"Sumnow for {a:b}and {b:b},\tres: {res:b} ctr\t{ctr:b}\t new bit {res_b:b}")

    res, ctr, carry = add_overfill(a, res, ctr, carry)
    res, ctr, carry = add_overfill(b, res, ctr, carry)

    if carry:
        # print(f"Carry at the end, to {res:b}")
        res ^= raise_to_counter(0b1, ctr)

    return res


def add_no_alg_better(a, b):
    if b == 0:
        return a

    just_sum = a ^ b
    carry = (a & b) << 1

    return add_no_alg_better(just_sum, carry)


if __name__ == "__main__":
    exs = [(x, y) for x in range(1000) for y in range(1000)]
    # exs = [(0b1011, 0b1011)]
    fails = 0
    for a, b in exs:
        if add_no_alg(a, b) != a + b or add_no_alg_better(a, b) != a + b:
            print(
                f"Result\t{add_no_alg(a,b):b}," 
                f"same as\t{(a+b):b} ? {add_no_alg(a,b) == a+b}, for inputs {a:b} and {b:b}"
            )
            fails += 1
            print("*" * 50)
        else:
            # print(f"Good for {a} and {b}")
            pass
