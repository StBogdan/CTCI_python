from chapter_2.linked_list_utils import Node, llol


def check_ll_palindrome(h: Node):
    sl_len = -1
    fst_len = -1

    if not h:
        return True

    slp = h
    fstp = h
    stack = []
    while fstp:
        sl_len += 1
        fst_len += 2
        stack.append(slp.val)

        slp = slp.next
        fstp = fstp.next

        if fstp:
            fstp = fstp.next
            if not fstp:
                fst_len += 1

    if fst_len > 0 and fst_len % 2:
        stack.pop()

    print(f"Stack is {stack}, slp is {slp}")

    while slp:
        if slp.val != stack.pop():
            return False
        slp = slp.next

    return not stack


if __name__ == "__main__":

    exs = [
        [],
        [4],
        [1, 2, 2],
        [1, 2, 3, 4],
        [1, 1, 2, 1],
        [1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 0, 2, 1],
    ]

    for ex in exs:
        h_ex = llol(ex) if ex else None
        print(f"Result for {ex} is {check_ll_palindrome(h_ex)}")
        print("-"*50)
