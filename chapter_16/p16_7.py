
def sign(a: int):
    return (a >> 32) & 0b1


def max_unconditional(a, b):
    diff = a - b

    both_negate = (sign(a)) & (sign(b))
    sign_flag = sign(diff) ^ (not both_negate)
    # print(f"Are both {a} and {b} negative {both_negate:b},\t"
    #       f"with signs {sign(a)} and {sign(b)}\t"
    #       f"Sign flag is {sign_flag}")
    return ((not sign_flag) * a) | ((sign_flag) * b)


if __name__ == "__main__":
    exs = [
        (10, 20),
        (20, 10),
        (-10, -20),
        (20, -10),
        (-20, -10),
        (0, 10),
        (-20, 0),
    ]

    for a, b in exs:
        print(f"Max of {a} and {b} is:\t"
              f"{max_unconditional(a,b)} == {max(a,b)}")
