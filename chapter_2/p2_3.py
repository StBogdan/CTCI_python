from chapter_2.linked_list_utils import llol, Node


def remove_mid(mid_node: Node):
    victim = mid_node.next
    if not victim:
        raise Exception("No following nodes")

    # Take the value, and point to the next (can be none)
    mid_node.val = victim.val
    mid_node.next = victim.next
    victim.next = None


if __name__ == "__main__":
    exs = [([1, 2, 3, 4, 5], 3),
           ([1, 1, 1, 1], 1),
           ([1, 2, 4, 5, 6, 7], 2),
           ([1, 2, 3], 3)]

    for arr, elem in exs:
        head = llol(arr)
        in_node = head
        while in_node.val != elem:
            in_node = in_node.next

        try:
            remove_mid(in_node)
            print(f"For input {arr} to remove {elem} got result {head}")
        except Exception as e:
            print(f"For input {arr} to remove {elem} got error: {e}")
        print("-"*50)
