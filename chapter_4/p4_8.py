from utils.graphs import BiNode, ltbt
from typing import Tuple, Optional
from utils.treeviz import viz_tree

# No parent, method 1 with covers


def first_common_ancestor(r: BiNode, e1: int, e2: int):
    res_1 = com_anc_covers(r, e1, e2)
    res_2 = com_anc_helper(r, e1, e2)

    print(f"Common anc, method 1 : {res_1}, "
          f"method 2: {res_2[0].val if res_2[1] else 'Not found'}")
    return res_2[0].val if res_2[1] else None


def com_anc_covers(n: BiNode,
                   e1: int,
                   e2: int) -> Optional[int]:
    if not n:
        return None

    # If both are covered by the left/right subtree,
    # Look for solution there
    rc1 = covers(n.right, e1)
    rc2 = covers(n.right, e2)
    if rc1 and rc2:
        return com_anc_covers(n.right, e1, e2)

    lc1 = covers(n.left, e1)
    lc2 = covers(n.left, e2)
    if lc1 and lc2:
        return com_anc_covers(n.left, e1, e2)

    # If current is one of them, and the other in a subtree
    if (n.val == e1 and (lc2 or rc2)) or (n.val == e2 and (lc1 or rc1)):
        return n.val

    # If e1 and e2 covered by different subtrees, this is the place
    if (rc1 ^ rc2) and (lc1 ^ lc2):
        return n.val


def covers(root: BiNode, elem: int):
    if not root:
        return False
    if root.val == elem:
        return True
    else:
        return covers(root.left, elem) or covers(root.right, elem)

# No parent, method 2
# Send up the result of current search


def com_anc_helper(root: BiNode,
                   e1: int,
                   e2: int) -> Tuple[Optional[BiNode], Optional[bool]]:
    if not root:
        return (None, None)

    # If the ancestor is in the left (or right)subtree,
    # return that

    left_res, left_has_anc = com_anc_helper(root.left, e1, e2)
    if left_res and left_has_anc:
        return (left_res, left_has_anc)

    right_res, right_has_anc = com_anc_helper(root.right, e1, e2)
    if right_res and right_has_anc:
        return (right_res, right_has_anc)

    # If both nodes found in the left and right trees
    # But not ancestors, this is the ancestor
    if left_res and right_res:
        return (root, True)
    else:
        if (root.val == e1 or root.val == e2):
            # Current is one of them and the other in subtrees
            is_anc = (left_res or right_res)
            return (root, is_anc)
        else:
            # Send up if one of target nodes found
            return (left_res if left_res else right_res, False)


if __name__ == "__main__":
    ex = [2, 10, 30, 55, 15, None, None, 3, 37, None, 17]
    root = ltbt(ex)
    viz_tree(root)

    first_common_ancestor(root, 17, 37)
    first_common_ancestor(root, 17, 37)
    first_common_ancestor(root, 55, 3)
    first_common_ancestor(root, 3, 55)
    first_common_ancestor(root, 2, 9999)