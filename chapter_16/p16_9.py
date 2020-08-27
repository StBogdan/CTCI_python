def substract(a: int, b: int) -> int:
    return a + flip_sign(b)


def multiply(a: int, b: int) -> int:
    c_sum = 0
    negative_other = b < 0

    if negative_other:
        b = flip_sign(b)

    for _ in range(b):
        c_sum += a

    return c_sum if not negative_other else flip_sign(c_sum)


def divide(a: int, b: int) -> int:
    if b == 0:
        raise Exception("Cannot do zero division")

    is_a_neg = a < 0
    is_b_neg = b < 0

    if is_a_neg:
        a = flip_sign(a)
    if is_b_neg:
        b = flip_sign(b)

    cprod = 0
    x = -1
    while cprod < a:
        x += 1
        cprod += b

    return x if not is_a_neg ^ is_b_neg else flip_sign(x)


def flip_sign(a: int):
    diff_driver = -1 if a > 0 else 1
    new_a = 0
    while a:
        a += diff_driver
        new_a += diff_driver

    return new_a


if __name__ == "__main__":
    exs = [
        (10, 3),
        (10, -3),
        (-10, 3),
        (-10, -3),
        (-3, 12)
    ]

    for a, b in exs:
        print(f" {a} / {b} = {divide(a,b)}, {a} * {b} = {multiply(a,b)}")
