from chapter_2.linked_list_utils import *

# Method: Leader and follower pointer, at k distance
# Time: O(n)
# Space: O(1)


def k_to_last(k: int, head: Node):
    leader_ptr = head
    follower_ptr = head
    distance = -1

    while leader_ptr:
        print(f"Leader is {leader_ptr} "
              f"and follower {follower_ptr},"
              f" at distance {distance}")
        distance += 1
        if distance > k:
            follower_ptr = follower_ptr.next
        leader_ptr = leader_ptr.next

    if distance < k:
        raise Exception(f"Input too short for distance {distance}")

    return follower_ptr.val


if __name__ == "__main__":
    ex1 = link_list_of_list([1, 2, 3, 4, 5, 6, 7])
    d = 5
    print(ex1)
    print(k_to_last(d, ex1))
