from chapter_2.linked_list_utils import Node, link_list_of_list, lllen, llol


def get_intersecting_node(h1: Node, h2: Node):
    ll1 = lllen(h1)
    ll2 = lllen(h2)

    if get_last_of_ll(h1) != get_last_of_ll(h2):
        return None

    if ll1 > ll2:
        sl = h2
        bl = h1
    else:
        sl = h1
        bl = h2

    bl = adjust(bl, abs(ll1 - ll2))
    while bl != sl:
        bl = bl.next
        sl = sl.next
    return bl.val


def adjust(head: Node, jumps):
    h = head
    for _ in range(jumps):
        h = h.next
    return h


def get_last_of_ll(head_in: Node):
    h = head_in
    while h.next:
        h = h.next
    return h


if __name__ == "__main__":
    exs = [([1, 2, 3, 4, 5, 6], [10, 20, 30], 4),
           ([1, 2, 3, 4, 5], [11, 22, 33, 44], 4),
           ([1, 2], [32, 43, 54, 65, 76], 1)]
    for a1, a2, con_point in exs:
        ll1 = llol(a1)
        ll2 = llol(a2)

        last_of_2 = get_last_of_ll(ll2)
        last_of_2.next = adjust(ll1, con_point)

        print(f"For lists {a1} and {a2} joined at {con_point}, \
             intersect node is : {get_intersecting_node(ll1,ll2)}")
