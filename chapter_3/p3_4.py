from chapter_3.datastructs import Stack

class MyQueue:
    s_in = Stack()
    s_out = Stack()
    
    def push(self, elem: int):
        self.s_in.push(elem)

    def pop(self):
        if self.s_out.isEmpty():
            self._pour(self.s_in, self.s_out)
        return self.s_out.pop()

    def isEmpty(self):
        return self.s_in.isEmpty() and self.s_out.isEmpty()

    def peek(self):
        if self.s_out.isEmpty():
            self._pour(self.s_in, self.s_out)
            self.s_out.peek()

    def size(self):
        return self.s_in.size + self.s_out.size
    
    @staticmethod
    def _pour(s_from:Stack, s_to:Stack):
        while not s_from.isEmpty():
            s_to.push(s_from.pop())
    
    def __str__(self):
        return f"Ha! I'm actually 2 stacks: {self.s_in} and {self.s_out}"


def test_myQueue():
    myq = MyQueue()
    for i in range(5):
        myq.push(i)
    
    print(f"Is empty ? {myq.isEmpty()} ---> {myq}")

    for i in range(5):
        print(myq.pop())
    
    try:
        myq.pop()
    except Exception as e:
        print(f"Oh no, got {e}, but queue has elem ? {not myq.isEmpty()}")

    for i in range(10,15):
        myq.push(i)  
    
    print(myq.pop())

    for i in range(15,20):
            myq.push(i)  
    print(myq)

if __name__ == '__main__':
    test_myQueue()
    