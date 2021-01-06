from chapter_2.linked_list_utils import Node, llol

# Method: Slow/Fast pointer, push to stack second half and check
# Time: O(n)
# Space: O(n)


def check_ll_palindrome(head: Node):
    slow_len = -1
    fast_len = -1

    if not head:
        return True

    slow_ptr = head
    fast_ptr = head
    stack = []
    while fast_ptr:
        slow_len += 1
        fast_len += 2
        stack.append(slow_ptr.val)

        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

        if fast_ptr:
            fast_ptr = fast_ptr.next
            if not fast_ptr:
                fast_len += 1

    if fast_len > 0 and fast_len % 2:
        stack.pop()

    print(f"Stack is {stack}, slp is {slow_ptr}")

    while slow_ptr:
        if slow_ptr.val != stack.pop():
            return False
        slow_ptr = slow_ptr.next

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
