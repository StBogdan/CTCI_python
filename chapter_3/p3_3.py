from chapter_2.linked_list_utils import Node
from typing import List
from chapter_3.datastructs import Stack


class SetOfStacks:
    STACK_CAP = 10

    def __init__(self):
        self.stacks: List[Stack] = []  # Stack vector
        self.size = 0
        self.top = None

    def pop(self):
        if self.size == 0:
            raise Exception("Empty Stack")

        if self.stacks[-1].size % self.STACK_CAP == 1:  # One till we go down
            ret_val = self.stacks[-1].pop()

            self.stacks.pop()

            # Backpedal until non-empty stack
            i = 1
            while self.stacks and self.stacks[-i].isEmpty():
                i += 1
                self.stacks.pop()

        else:
            ret_val = self.stacks[-1].pop()
        self.size -= 1
        return ret_val

    def pop_at(self, index: int):
        if index > len(self.stacks):
            raise Exception("Invalid stack index")

        stack_target: Stack = self.stacks[index]

        if not stack_target.isEmpty():
            ret_val = stack_target.pop()
            self.size -= 1
        else:  # That stack empty
            raise Exception(f"Empty sub stack for {index}")
        return ret_val

    def push(self, elem: int):
        if not self.stacks:
            self.stacks.append(Stack())
            self.stacks[0].push(elem)
        else:
            last_stack = self.stacks[-1]
            if last_stack.size % self.STACK_CAP == 0:
                self.stacks.append(Stack())
                self.stacks[-1].push(elem)
            else:
                last_stack.push(elem)

        self.size += 1

    def __str__(self):
        return "\n".join(
            [f"Stackset with {len(self.stacks)} stacks, size {self.size}, as follows:"]
            + list(map(str, self.stacks))
            + ["*" * 50])


if __name__ == "__main__":
    sos = SetOfStacks()
    # Initial build
    for i in range(100):
        sos.push(i)
    print(sos)

    # Pop one from each, but from 5 more
    for i in range(10):
        if i == 5:
            for j in range(5):
                sos.pop_at(i)
        print(f"From stack {i}, got elem {sos.pop_at(i)}")
    
    # Push 2 more elements
    sos.push(99)
    sos.push(100)
    print(sos)
