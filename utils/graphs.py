from typing import List

class BiNode:
    val: int = None
    left = None
    right = None

    def __str__(self):
        return f"({self.left if self.left else '_' }/{self.val}\\{self.right if self.right else '_'})"

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ltbt(arr: List[int]) -> BiNode:
    return list_to_binary_tree(arr)


def list_to_binary_tree(arr: List[int]) -> BiNode:
    nodes = [BiNode(arr[0])]
    for i in range(1, len(arr)):
        parent = nodes[(i - 1)//2]

        node_now = BiNode(arr[i])
        nodes.append(node_now)
        if (i-1) % 2:
            parent.right = node_now
        else:
            parent.left = node_now

    return nodes[0]
