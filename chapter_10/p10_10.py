from utils.graphs import BiNode
from utils.treeviz import viz_tree


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


class NumberTracker:

    def __init__(self):
        self.root = None

    def track(self, x: int):
        if not self.root:
            self.root = SizedNode(x)
        else:
            self.root.insert(x)

    def getRankOfNumber(self, x: int) -> int:
        return self._rank_helper(self.root, x)

    @staticmethod
    def _rank_helper(node: SizedNode, val: int):
        if not node:
            return 0
        size_left = node.left.size if node.left else 0
        size_right = node.right.size if node.right else 0

        if val == node.val:
            return size_left
        elif val < node.val:
            return NumberTracker._rank_helper(node.left, val)
        else:
            # This subtree, minus the elements in the right one (which we will fill in)
            return node.size - size_right + NumberTracker._rank_helper(node.right, val)


if __name__ == "__main__":
    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    nt = NumberTracker()
    for x in stream:
        nt.track(x)

    viz_tree(nt.root)
    target_nums = [1, 3, 4, 5, 14]
    for num in target_nums:
        print(f"Rank of number {num} is {nt.getRankOfNumber(num)}")
