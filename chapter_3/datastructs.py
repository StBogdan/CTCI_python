from chapter_2.linked_list_utils import Node


class Stack:
    top: Node = None
    size: int = 0

    def push(self, elem):
        self.size += 1
        if not self.top:
            self.top = Node(elem)
        else:
            new_node = Node(elem)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("Cannot pop from an empty stack")

        self.size -= 1

        ret_elem = self.top.val
        self.top = self.top.next
        return ret_elem

    def peek(self):
        return self.top.val

    def isEmpty(self):
        return self.top is None

    def __str__(self):
        return self.top.__str__()


class Queue:
    top: Node = None
    bot: Node = None
    size: int = 0

    def push(self, elem):
        self.size += 1
        if not self.top:
            self.top = Node(elem)
            self.bot = self.top
        else:
            new_node = Node(elem)
            self.top.next = new_node
            self.top = new_node

    def pop(self):
        if not self.bot:
            raise Exception("Cannot pop from an empty queue")

        self.size -= 1

        ret_elem = self.bot.val
        self.bot = self.bot.next
        if self.bot is None:
            self.top = None

        return ret_elem

    def peek(self):
        return self.bot.val

    def isEmpty(self):
        return self.bot is None

    def __str__(self):
        return self.bot.__str__()


def test_stack():
    s1 = Stack()
    for i in range(10):
        s1.push(i)

    print(s1)
    for i in range(10):
        print(s1.pop())

    try:
        s1.pop()
    except Exception as e:
        print(f"Oh no, got {e}")


def test_queue():
    q1 = Queue()
    for i in range(5):
        q1.push(i)

    print(f"Is empty ? {q1.isEmpty()} ---> {q1}")

    for i in range(5):
        print(q1.pop())

    try:
        q1.pop()
    except Exception as e:
        print(f"Oh no, got {e}, but queue has elem ? {q1.isEmpty()}")

    for i in range(5):
        q1.push(i)

    print(q1.pop())


if __name__ == '__main__':
    test_stack()
    test_queue()
