from utils.graphs import BiNode, ltbt
from utils.treeviz import viz_tree


def check_balanced(root: BiNode):
    return check_bal_rec(root) > 0


def check_bal_rec(node: BiNode):
    if not node:
        return 0

    depth_right = check_bal_rec(node.right)
    depth_left = check_bal_rec(node.left)
    if depth_right < 0 or depth_left < 0:
        return -1
    elif abs(depth_right-depth_left) > 1:
        return -1
    else:
        return max(depth_right, depth_left) + 1


if __name__ == "__main__":
    extree = ltbt([0, 11, 12, 21, 222, 55, None, 31, 21, None, 42])
    viz_tree(extree)
    resp = check_balanced(extree)
    print(f"Is tree balanced {resp}")
