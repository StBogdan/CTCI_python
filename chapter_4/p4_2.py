from typing import List
from utils.graphs import BiNode
from utils.treeviz import *
# CTCI 4.2

# Random links
# https://orth.uk
# https://foodprint.orth.uk  for software engineering project

# https://devwebcl.blogspot.com/2016/12/big-o-comparison.html
# https://awwapp.com/b/umyxkgethk506/


def main():
    # ordered_list = [1, 2, 3, 6]
    ordered_list = [1, 2, 3, 6, 10, 12, 15, 16]
    print(ordered_list)
    result = create_binary_from_sorted_arr(ordered_list)
    viz_tree(result)
    print(result)


def create_binary_from_sorted_arr(arr: List[int]) -> BiNode:
    if (len(arr) == 0):
        return None
    if (len(arr) == 1):
        return BiNode(arr[0], None, None)

    # pick out middle number
    middle_index = len(arr) // 2

    # recursively call
    left = create_binary_from_sorted_arr(arr[0:middle_index])
    right = create_binary_from_sorted_arr(arr[middle_index + 1:])
    return BiNode(arr[middle_index], left, right)


if __name__ == "__main__":
    main()
