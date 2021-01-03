from typing import List

# Method: Count spaces, move into place from the end
# Time: O(n)
# Space: O(1)


def urlize(a: List[chr], true_len):
    ei = true_len - 1

    nr_spaces = 0
    for i in range(true_len):
        if a[i] == " ":
            nr_spaces += 1

    ei = true_len - 1 - (nr_spaces//3) * 2
    # print(f"Turns out the string starts at {ei}")
    end_i = true_len-1
    while ei >= 0:
        # print(f"Not at {ei} and outputloc {end_i}")
        if a[ei] != " ":
            a[end_i] = a[ei]
        else:
            a[end_i] = "0"
            a[end_i-1] = "2"
            a[end_i-2] = "%"
            end_i -= 2
        end_i -= 1
        ei -= 1
    return "".join(a)


def get_prob_input(str_w_spaces: str) -> str:
    """Add the necessary buffer at the end, for a normal str
    """
    spaces = str_w_spaces.count(" ")
    return str_w_spaces + " " * (spaces * 2), len(str_w_spaces) + spaces*2


if __name__ == "__main__":
    example1 = "Taco cat is evil"
    a, fn = get_prob_input(example1)
    print(f"Input is |{a}|, result |{urlize(list(a), fn)}| ")

    a, fn = get_prob_input(" a")
    print(f"Input is |{a}|, result |{urlize(list(a), fn)}| ")

    a, fn = get_prob_input(" a c    a    c")
    print(f"Input is |{a}|, result |{urlize(list(a), fn)}| ")
