from typing import List

english_spellings = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

group_separators = ["", "thousand", "million", "billion", "trillion"]


def two_digits_to_str(digit_list_rev: List[int]) -> str:
    x = digit_list_rev[1] * 10 + digit_list_rev[0]
    if 19 < x:
        ans = english_spellings[digit_list_rev[1]*10]
        if digit_list_rev[0]:
            ans += "-" + english_spellings[digit_list_rev[0]]
        return ans
    elif x < 10:
        return english_spellings[x % 10]
    else:
        return english_spellings[x]


def triple_to_string(triple_list_rev: List[int]) -> str:
    if not triple_list_rev or all(x == 0 for x in triple_list_rev):
        return ""

    # Add padding if necessary
    if len(triple_list_rev) < 3:
        triple_list_rev = triple_list_rev + [0] * (3 - len(triple_list_rev))

    res = []
    if triple_list_rev[2]:
        res.append(f"{english_spellings[triple_list_rev[2]]} hundred")

    if any(triple_list_rev[:2]):  # There are non-zero digits
        res.append(two_digits_to_str(triple_list_rev[:2]))

    return " ".join(res)

def get_digit_list(x:int) -> List[int]:
    digits =[]
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits


def int_to_eng(x: int):
    if x < 10:
        return english_spellings[x]

    x_digits = get_digit_list(x)

    if len(x_digits) == 4:
        return " ".join([two_digits_to_str(x_digits[2:]), two_digits_to_str(x_digits[:2])])

    end_str_parts = []
    triplets = [x_digits[i: i+3] for i in range(0, len(x_digits), 3)]

    for i, tripl in enumerate(triplets):
        tripl_str = triple_to_string(tripl)
        if tripl_str:
            end_str_parts.append(
                f"{triple_to_string(tripl)} {group_separators[i]}")

    return " ".join(end_str_parts[::-1])


if __name__ == "__main__":
    exs = [
        1,
        0,
        10,
        20,
        4959,
        2020,
        1945,
        123_456_000_789_055,
        100_020_003,
        101_880
    ]
    for x in exs:
        print(f"În engleză {x} este {int_to_eng(x)}")
