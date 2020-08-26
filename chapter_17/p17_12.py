
class BiNode:
    def __init__(self, val):
        self.val = val
        self.node1 = None
        self.node2 = None


def flatten_binary_tree(root: BiNode):
    left_side, _ = flat_helper(root)
    return left_side


def flat_helper(root: BiNode) -> tuple:
    left_edge = root
    right_edge = root
    if root.node1:
        left_edge_left, left_edge_right = flat_helper(root.node1)

        root.node1 = left_edge_right
        left_edge_right.node2 = root

        left_edge = left_edge_left
    if root.node2:
        right_edge_left, right_edge_right = flat_helper(root.node2)

        root.node2 = right_edge_left
        right_edge_left.node1 = root

        right_edge = right_edge_right

    return (left_edge, right_edge)


#	20
#  10       25
# 5        22
#	  21   23

if __name__ == "__main__":
    root = BiNode(20)
    root.node1 = BiNode(10)
    root.node1.node1 = BiNode(5)
    root.node2 = BiNode(25)
    root.node2.node1 = BiNode(22)
    root.node2.node1.node2 = BiNode(23)
    root.node2.node1.node1 = BiNode(21)

    list_start = flatten_binary_tree(root)

    list_elem_now = list_start
    while list_elem_now.node2:
        print(list_elem_now.val)
        list_elem_now = list_elem_now.node2
