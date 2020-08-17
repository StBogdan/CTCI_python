from utils.graphs import BiNode
from utils.treeviz import viz_tree
import random

class SizedNode(BiNode):
    def __init__(self, val: int):
        super().__init__(val)
        self.size = 1

    def insert(self, x: int):
        if x > self.val:
            if self.right:
                self.right.insert(x)
            else:
                self.right = SizedNode(x)
        else:
            if self.left:
                self.left.insert(x)
            else:
                self.left = SizedNode(x)
        self.size += 1


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, x: int):
        if not self.root:
            self.root = SizedNode(x)
        else:
            self.root.insert(x)

    def getRandomNuber(self) -> int:
        target = random.randint(1, self.root.size)
        print(f"Target is {target}")
        return self._get_inorder_number(self.root, target)

    def _get_inorder_number(self, node: SizedNode, target:int) -> int:
        right_size = node.right.size if node.right else 0
        # print(f"Node is {node.val}\tsize is {node.size},\tright is {right_size}")
        node_traversal_poz = node.size - right_size
        # print(f"At poz {node_traversal_poz},\ttarget is target {target}")
        if node_traversal_poz == target:
            return node.val
        elif node_traversal_poz < target:
            return self._get_inorder_number(node.right, target - node_traversal_poz)
        else:
            return self._get_inorder_number(node.left, target) 


if __name__ == "__main__":
    stream = [5, 1, 4, 14, 15, 9, 7, 13, 3]
    rbst = BinarySearchTree()
    for x in stream:
        rbst.add(x)

    viz_tree(rbst.root)
    print(rbst.root.size)
    print(f"Getting a random node: {rbst.getRandomNuber()}")
