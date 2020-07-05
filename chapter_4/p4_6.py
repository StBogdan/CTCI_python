from utils.graphs import BiPaNode, get_node_by_val, ltbt
from utils.treeviz import viz_tree
from typing import Optional


def next_in_order(node: BiPaNode) -> Optional[BiPaNode]:
    if node.right:  # Case 1, there's right subtree
        ans = node.right
        while ans.left:
            ans = ans.left
        return ans

    # Case 2, go up until not left child
    p = node.parent
    if p.left == node:
        return p
    else:  # Case 3, current is right child
        while p.parent:
            if (p.parent.right == p):
                p = p.parent
            else:
                return p.parent

    return None


if __name__ == "__main__":
    root = ltbt(range(7))
    viz_tree(root)
    exs = [0, 1, 2, 3, 4, 5, 6]
    for ex in exs:
        next_node = next_in_order(get_node_by_val(root, ex))
        next_val = next_node.val if next_node else -1
        print(
            f"For node {ex}, next val is {next_val}")
