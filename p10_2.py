from collections import Counter, defaultdict
from typing import List


def group_anag(arr: List[str]):
    buckets = defaultdict(list)
    res = []

    for a in arr:
        elems_a = Counter(a)
        id_a = tuple(sorted(elems_a.items()))
        buckets[id_a].append(a)

    for id_str, ang_list in buckets.items():
        # print(ang_list, end=" --- ")
        res.extend(ang_list)
    # print()
    return res


if __name__ == "__main__":
    example1 = ["aabb", "cabt", "baab", "tbac", "bbaa", "tbba"]
    example2 = ["cccc", "ddddd", "avca", "vcaa", "wwqwq", "aacv"]
    print(group_anag(example1))
    print(group_anag(example2))
