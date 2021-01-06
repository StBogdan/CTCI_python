from chapter_2.linked_list_utils import Node, lllen, llol

# Backward oder (head at least significant)
# Method: Digit by digit, with carry
# Time: O(n)
# Space: O(n) (Constant if you overwrite one of the inputs)

# Forward order
# Method: Pad to len, recurse down
# Time: O(n)
# Space: O(n)


def sum_ll(tl1: Node, tl2: Node):
    nl = None
    nlh = None
    carry_flag = 0

    if lllen(tl1) < lllen(tl2):
        tl1, tl2 = tl2, tl1

    while tl1 and tl2:
        dsum = tl1.val + tl2.val + carry_flag

        carry_flag = dsum // 10
        dsum %= 10

        if not nl:
            nl = Node(dsum)
            nlh = nl
        else:
            nl.next = Node(dsum)
            nl = nl.next

        tl1 = tl1.next
        tl2 = tl2.next

    while tl1:  # The longer one
        cval = tl1.val + carry_flag
        carry_flag = cval // 10
        cval %= 10

        nl.next = Node(cval)
        nl = nl.next

        tl1 = tl1.next

    if tl1 is None and carry_flag:
        nl.next = Node(1)

    return nlh


# The follow up, linked list is in reverse order
def pad_to_len(head, to_pad):
    for _ in range(to_pad):
        n = Node(0)
        n.next = head
        head = n
    return head


def sum_ll_reverse(tl1, tl2):
    len1 = lllen(tl1)
    len2 = lllen(tl2)

    if len1 > len2:
        tl2 = pad_to_len(tl2, len1-len2)
    elif len2 != len1:
        tl1 = pad_to_len(tl1, len2-len1)

    res, carry = sum_ll_rec(tl1, tl2)
    if carry:
        n = Node(1)
        n.next = res
        return n
    else:
        return res


def sum_ll_rec(tl1, tl2):
    if tl1 is None and tl2 is None:
        return None, 0
    rest, carry = sum_ll_rec(tl1.next, tl2.next)

    cval = tl1.val + tl2.val + carry
    head = Node(cval % 10)

    head.next = rest
    return head, cval//10


if __name__ == "__main__":
    exs = [([1, 2, 3, 4, 5], [1, 2, 3]),
           ([9, 9, 9, 9], [2, 1]),
           ([9], [1])]

    for l1, l2 in exs:
        print(f"Backward result of sum of\t {l1} and {l2} is {sum_ll(llol(l1), llol(l2))}"
              f" same as {sum_ll(llol(l2), llol(l1))}")

        ll1r = llol(list(reversed(l1)))
        ll2r = llol(list(reversed(l2)))

        print(f"Forward result of sum of\t {l1} and {l2} is {sum_ll_reverse(llol(l1), llol(l2))}"
              f" same as {sum_ll_reverse(llol(l2), llol(l1))}")
        print("-"*50)


