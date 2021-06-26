from typing import List
import math
import copy
import random

# Method: Use math
# Time: O(n)
# Space: O(1)
# Note: For 2 numbers, we can get a + b  and a^2 + b^2
#  (a + b) ^ 2 = a^2 + 2ab  + b^2

TRIALS = 10


def find_two_missing(arr: List[int], N: int) -> List[int]:
    # print(f"Array of len {len(arr)} is {arr}")
    all_sum = sum(range(1, N + 1))
    all_quad_sum = sum(i ** 2 for i in range(1, N + 1))

    real_sum = sum(arr)
    real_quad_sum = sum(x ** 2 for x in arr)

    delta_sum = all_sum - real_sum
    delta_quad_sum = all_quad_sum - real_quad_sum

    b = int((delta_sum + math.sqrt(2 * delta_quad_sum - delta_sum ** 2)) / 2)
    a = int((delta_sum ** 2 - delta_quad_sum) / (2 * b))

    return [a, b]


def get_indexes_to_remove(N: int) -> tuple:
    a = random.randint(0, N - 1)
    b = random.randint(0, N - 1)
    while b == a:
        b = random.randint(0, N - 1)

    return (a, b)


if __name__ == "__main__":
    N = 100
    all_arr = list(range(1, N + 1))

    for i in range(TRIALS):
        test_arr = copy.copy(all_arr)
        i1, i2 = get_indexes_to_remove(N)

        a, b = test_arr[i1], test_arr[i2]

        test_arr = [test_arr[i] for i in range(len(test_arr)) if i not in {i1, i2}]

        print(f"Missing from arr are {find_two_missing(test_arr,N)}, expected {a}, {b}")
