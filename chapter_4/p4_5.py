from utils.graphs import ltbt, BiNode
from utils.treeviz import viz_tree


def check_bst(root: BiNode):
    print(f"Checking bst, got result of ranging: {get_tree_range(root)}")
    return not get_tree_range(root)[0] is False


def get_tree_range(n: BiNode) -> tuple:
    if n is None:
        return (None, None)
    else:
        range_l = get_tree_range(n.left)
        range_r = get_tree_range(n.right)

        if range_l[0] is False or range_r[0] is False:
            return (False, False)

        if check_bst_condition(n.val, range_l[1], range_r[0]):
            range_min = min(range_l[0], n.val) \
                if range_l[0] is not None else n.val
            range_max = max(range_r[1], n.val) \
                if range_r[1] is not None else n.val
            return (range_min, range_max)
        else:
            return (False, False)


def check_bst_condition(val, max_left, min_right):
    return (not max_left or max_left <= val) \
        and (not min_right or val < min_right)


if __name__ == "__main__":
    extree = ltbt([100, 50, 150, 25, 99, None, 300] + [None] * 6 + [175 , 301])
    print(extree)
    viz_tree(extree)
    resp = check_bst(extree)
    print(f"Is tree a binary search tree ? {resp}")
