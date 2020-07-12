from chapter_3.datastructs import Stack

MAX_INT = 2**32-1


class MinStack:
    def __init__(self):
        self.stack = Stack()

    def pop(self):
        return self.stack.pop()[0]

    def min(self):
        if self.stack.isEmpty():
            raise Exception("Empty stack has no minimum")

        _, min_elem = self.stack.peek()
        return min_elem

    def push(self, elem):
        current_min = self.min() if not self.stack.isEmpty() else MAX_INT

        nmin = min(elem, current_min)
        self.stack.push((elem, nmin))


if __name__ == "__main__":
    min_stack = MinStack()
    for i in range(10):
        min_stack.push(10-i)

    print(min_stack)
    for i in range(9):
        print(
            f"Got from stack elem {min_stack.pop()}, minimum is now {min_stack.min()}")
