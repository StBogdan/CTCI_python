class Node:
    val: int
    next = None

    def __init__(self, val, next_node=None):
        self.val = val
        self. next = next_node

    def __str__(self):
        return f"({self.val}) -> {self.next!r}"


def link_list_of_list(arr) -> Node:
    head = Node(arr[0])
    now_elem = head
    for x in arr[1:]:
        now_elem.next = Node(x)
        now_elem = now_elem.next
    return head


if __name__ == "__main__":
    ex1 = [1, 2, 3]
    print(link_list_of_list(ex1))
