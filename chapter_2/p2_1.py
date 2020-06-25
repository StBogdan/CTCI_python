from chapter_2.linked_list_utils import Node, llol


def remove_dups_ll(head: Node):
    seen = set()
    prev = None
    while head:
        if head.val in seen:
            prev.next = head.next
        else:
            seen.add(head.val)
        prev = head
        head = head.next


def remove_dups_nobuf(h: Node):
    rc = h
    while rc:
        target = rc.val
        prev = rc
        restp = rc.next
        while restp:
            if restp.val == target:
                prev.next = restp.next
            else:
                prev = restp
            restp = restp.next
        rc = rc.next


if __name__ == "__main__":
    exs = [[1, 2, 3, 4, 5],
           [11, 2, 3, 4, 5, 6, 11],
           [11, 2, 3, 4, 5, 6, 11, 11, 11, 23],
           [0],
           [0, 0],
           [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 3, 1]]

    for ex in exs:
        r1 = llol(ex)
        r2 = llol(ex)
        remove_dups_nobuf(r1)
        remove_dups_nobuf(r2)
        print(f"For ex {ex} for ans 1: {r1}")
        print(f"For ex {ex} for ans 2: {r2}")
        print("-"*50)
