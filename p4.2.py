from typing import List
# CTCI 4.2


def main():
    # ordered_list = [1, 2, 3, 6]
    ordered_list = [1, 2, 3, 6, 10, 12, 15, 16]
    print(ordered_list)
    result = f"Result : {create_binary_from_sorted_arr(ordered_list)}"
    print(result)


class Node:
    val: int = None
    left = None
    right = None

    def __str__(self):
        return f"({self.left if self.left else '_' }/{self.val}\\{self.right if self.right else '_'})"

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

        # https://orth.uk
        # https://foodprint.orth.uk  for software engineering project


def create_binary_from_sorted_arr(arr: List[int]) -> Node:
    if (len(arr) == 0):
        return None
    if (len(arr) == 1):
        return Node(arr[0], None, None)

    # pick out middle number
    middle_index = len(arr) // 2

    # recursively call
    left = create_binary_from_sorted_arr(arr[0:middle_index])
    right = create_binary_from_sorted_arr(arr[middle_index + 1:])
    return Node(arr[middle_index], left, right)

    # https://devwebcl.blogspot.com/2016/12/big-o-comparison.html

# https://awwapp.com/b/umyxkgethk506/


if __name__ == "__main__":
    main()
