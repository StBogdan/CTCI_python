from utils.graphs import BiNode, ltbt


def maximum_perfect_tree(tree_root: BiNode):
    max_now = 0

    def max_perf_tree_depth(root: BiNode) -> int:
        nonlocal max_now
        if not root:
            return 0

        l_max = max_perf_tree_depth(root.left)
        r_max = max_perf_tree_depth(root.right)
        val_now = 1 + min(l_max, r_max)

        if val_now > max_now:
            max_now = val_now

        return val_now

    max_perf_tree_depth(tree_root)
    return 2**max_now -1


if __name__ == "__main__":
    tree_arr =      [1] +\
                [2,                 3] + \
            [None, 4] +            [5, 6] +\
    [None, None] + [None, None] + [7, 8] + [9, 10]
    [None] * 14 +                       [11]
    example_root = ltbt(tree_arr)
    print(f"Max tree is {maximum_perfect_tree(example_root)}")
