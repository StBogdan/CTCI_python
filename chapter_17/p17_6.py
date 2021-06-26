# Method: Math counting digit by digit
# Time: O(log(n))
# Space: O(1)

# Go digit by digit (keep dividing by higher powers of 10)
# At each stage, count *100 occurances in int div
# For ind mod, -> case 1, over 2: count all two's of the remainder
#              -> case 2, on 2: count all two's of the remainder of this level
#              -> case 3: below 2: no twos
# 25
# 9


def count_of_digit(x: int, digit=2):
    pow_10_now = 1
    digit_count = 0
    while x // pow_10_now > 0:
        # Left in the rest of the number (more significant digits)
        pow_10_next = pow_10_now * 10
        full_units = x // pow_10_next
        digit_count += (pow_10_now) * (full_units)

        remainder = x % pow_10_next
        rem_first_digit = remainder // pow_10_now

        if rem_first_digit > digit:
            digit_count += pow_10_now
        elif rem_first_digit == digit:
            digit_count += remainder % pow_10_now + 1

        # print(
        #     f"Cpow {cpow_10}, count_twos {count_digit}, full_units {full_units}, "
        #     f"remainder {remainder}, first digit {rem_first_digit}"
        # )

        pow_10_now *= 10
    return digit_count


def count_of_two(x: int):
    return count_of_digit(x, 2)


if __name__ == "__main__":
    for i in range(0, 1000, 50):
        print(f"For {i}, two's to it are {count_of_two(i)}")
