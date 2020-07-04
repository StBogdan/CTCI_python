from chapter_2.linked_list_utils import Node
from utils.graphs import BiNode, ltbt


def tree2LinkedList(root: BiNode):
    q = []
    ans = []

    q.append((root, 0))
    last_elem = None
    last_seen_level = 1

    while q:
        ce, lvl = q.pop(0)

        if lvl != last_seen_level:
            ans.append(Node(ce.val))
            last_seen_level = lvl
            last_elem = ans[lvl]
        else:
            last_elem.next = Node(ce.val)
            last_elem = last_elem.next

        for child in (ce.left, ce.right):
            if child is not None:
                q.append((child, lvl+1))

    return ans

if __name__ == "__main__":
    extree = ltbt(list(range(10)))
    resp = tree2LinkedList(extree)

    for ll in resp:
        print(ll)
