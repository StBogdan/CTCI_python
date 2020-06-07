class BiNode:
    val: int = None
    left = None
    right = None

    def __str__(self):
        return f"({self.left if self.left else '_' }/{self.val}\\{self.right if self.right else '_'})"

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right