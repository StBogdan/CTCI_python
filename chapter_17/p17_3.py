import random


def get_subset(arr, m):
    if m >= len(arr):
        raise Exception("Subset cannot be larger than array")
    subset = arr[:m]
    for i in range(m, len(arr)):
        place = random.randint(0, i)
        if place < m:
            subset[place] = arr[i]
    return subset


if __name__ == "__main__":
    arr = list(range(10))
    for i in range(5):
        print(get_subset(arr, 5))
