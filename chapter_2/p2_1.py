from chapter_2.linked_list_utils import Node, llol

# Method: Use a set
# Time: O(n)
# Space: O(n)

# Method (no buffer): Pick one, try to find in rest of linked list
# Time: O(n^2)
# Space: O(1)


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


def remove_dups_nobuf(head: Node):
    rc = head
    while rc:
        target = rc.val
        prev = rc
        rest_ptr = rc.next
        while rest_ptr:
            if rest_ptr.val == target:
                prev.next = rest_ptr.next
            else:
                prev = rest_ptr
            rest_ptr = rest_ptr.next
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
