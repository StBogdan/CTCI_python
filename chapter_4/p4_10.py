from utils.graphs import ltbt, BiNode


def check_same_tree(root1: BiNode, root2: BiNode) -> bool:
    if (not root1) and (not root2):
        return True
    elif (not root1) or (not root2):
        return False
    else:
        if root1.val != root2.val:
            return False
        else:
            return check_same_tree(root1.left, root2.left) \
                and check_same_tree(root1.right, root2.right)


def check_sub_tree(t1: BiNode, t2: BiNode) -> bool:
    if not t1:
        return False
    if t1.val == t2.val:
        return check_same_tree(t1, t2)
    else:
        return check_sub_tree(t1.left, t2) or check_sub_tree(t1.right, t2)


if __name__ == "__main__":
    tree1_list = [0, 10, 15, 20, 30, 25, 35] + [None] * 5 + [45]
    tree2_list = [10, 20, 30]

    t1 = ltbt(tree1_list)
    t2 = ltbt(tree2_list)

    print(f"Is t2 a subtree of t1 ? {check_sub_tree(t1,t2)}")
    print(f"Is t1 a subtree of t2 ? {check_sub_tree(t2,t1)}")
