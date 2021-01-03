from collections import Counter

# Method: Character map
# Time: O(n)
# Space: O(n)

# Follow-up
# Method: Sort and compare
# Time: O(n*log(n))
# Space: O(n)


def all_uniqs(input_str: str):
    ctr = Counter(input_str)

    for k, v in ctr.items():
        if v > 1:
            return False
    return True


def all_uniqs_no_datastruct(x: str):
    sorted_x = sorted(x)
    n = len(x)
    for i in range(1, n):
        if sorted_x[i-1] == sorted_x[i]:
            return False
    return True


if __name__ == "__main__":

    inputs = ["", "aaasodkc", "abbccdcss", "aaa", "b", "bdes"]

    for x in inputs:
        print(
            f"Input {x} result: {all_uniqs(x)} same as {all_uniqs_no_datastruct(x)}")
