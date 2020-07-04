from chapter_3.datastructs import Stack

def sort_stack_w_stack(s1: Stack) -> None:
    s2 = Stack()
    s2.push(s1.pop())

    while not s1.isEmpty():
        elem = s1.pop()
        # print(f"Looking at elem {elem}")
        nr_str = 0
        while not s2.isEmpty() and s2.peek() > elem:
            s1.push(s2.pop())
            nr_str += 1

        s2.push(elem)
        for _ in range(nr_str):
            s2.push(s1.pop())

    while not s2.isEmpty():
        s1.push(s2.pop())

if __name__ == '__main__':
    s1 = Stack()
    for elem in [1,50,20,10,-40,20,-30]:
        s1.push(elem)

    print(f"Before sort {s1}")
    sort_stack_w_stack(s1)
    print(f"After sort {s1}")
    
    