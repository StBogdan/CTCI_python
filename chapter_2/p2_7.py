from chapter_2.linked_list_utils import Node, link_list_of_list, lllen, llol

# Method: Find total lenght, walk together until meet
# Time: O(n)
# Space: O(1)


def get_intersecting_node(h1: Node, h2: Node):
    len_ll1 = lllen(h1)
    len_ll2 = lllen(h2)

    if get_last_of_ll(h1) != get_last_of_ll(h2):
        return None

    if len_ll1 > len_ll2:
        short_ll = h2
        longer_ll = h1
    else:
        short_ll = h1
        longer_ll = h2

    longer_ll = adjust(longer_ll, abs(len_ll1 - len_ll2))
    while longer_ll != short_ll:
        longer_ll = longer_ll.next
        short_ll = short_ll.next
    return longer_ll.val


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
