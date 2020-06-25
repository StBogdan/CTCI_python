from chapter_2.linked_list_utils import *


def k_to_last(k: int, h: Node):
    ldr = h
    folw = h
    d = -1

    while ldr:
        print(f"Ldr is {ldr} and folw {folw}")
        d += 1
        if d > k:
            folw = folw.next
        ldr = ldr.next

    if d < k:
        raise Exception(f"Input too short for distance {d}")

    return folw.val


if __name__ == "__main__":
    ex1 = link_list_of_list([1, 2, 3, 4, 5, 6, 7])
    d = 5
    print(ex1)
    print(k_to_last(d, ex1))
