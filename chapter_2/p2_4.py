from chapter_2.linked_list_utils import llol, Node


def part_around(x: int, head: Node):
    low_head = None
    high_head = None
    low_root = None
    high_root = None

    elem_now = head
    while elem_now:
        elem_next = elem_now.next
        if elem_now.val >= x:
            if not high_root:
                high_head = elem_now
                high_root = elem_now
            else:
                high_head.next = elem_now
                high_head = elem_now
        else:
            if not low_head:
                low_head = elem_now
                low_root = elem_now
            else:
                low_head.next = elem_now
                low_head = elem_now
        elem_now = elem_next

    if low_root:
        low_head.next = high_root  # Connect the parts
        high_head.next = None
        return low_root
    else:
        return high_root  # No low elems


if __name__ == "__main__":
    exs = [([1, 2, 3, 4, 5, 6, 7], 4),
           ([10, 4, 7, 3, 1, 200, 40, 50, 3], 4),
           ([30, 40, 50], 30),
           ([1, 2, 5, 3, 2, 200], 3)
           ]

    for arr, x in exs:
        head = llol(arr)
        print(
            f"For\t{head} around partition {x},\ngot\t{part_around(x, head)}")
        print("-"*50)
