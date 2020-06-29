from chapter_2.linked_list_utils import Node


def get_first_loop_elem(h: Node):
    if not h.next:
        return None

    slp = h.next
    fstp = h.next.next

    while fstp and slp != fstp:
        slp = slp.next
        fstp = fstp.next

        if not fstp:
            return None

        fstp = fstp.next
        print(f"Slow pointer at {slp.val}")

    if not fstp:
        return None

    slp2 = h

    while slp2 != slp:
        slp2 = slp2.next
        slp = slp.next

    return slp.val


if __name__ == "__main__":

    nodes = [Node(1)]
    for x in range(1, 10):
        nodes.append(Node(x))
        nodes[-2].next = nodes[-1]

    print(f"Got linked list {nodes[0]}")
    print(
        f"Does linked list have loop starting at ? \
             {get_first_loop_elem(nodes[0])}")
    nodes[-1].next = nodes[8]

    print(f"Does linked list have loop starting at ? \
         {get_first_loop_elem(nodes[0])}")
