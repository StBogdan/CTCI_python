from utils.graphs import BiNode, ltbt
from utils.treeviz import viz_tree
from collections import defaultdict


def paths_w_sum(root: BiNode, target: int) -> int:
    total_paths = 0

    def find_paths_down(r, t, sofarsum, prev):
        nonlocal total_paths
        if not r:
            return

        sum_now = prev + r.val
        if sum_now - t in sofarsum:
            total_paths += sofarsum[sum_now-t]

        sofarsum[sum_now] += 1
        find_paths_down(r.left, t, sofarsum, sum_now)
        find_paths_down(r.right, t, sofarsum, sum_now)
        sofarsum[sum_now] -= 1

    find_paths_down(root, target, defaultdict(lambda: 0), 0)
    return total_paths


if __name__ == "__main__":
    ex_tree = [10, 5, -3, 3, 2, 11, None, 3, -2, 1]
    root = ltbt(ex_tree)
    viz_tree(root)
    target = 8
    print(f"Paths to {target} are {paths_w_sum(root,target)}")
