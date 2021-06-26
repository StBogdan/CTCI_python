from typing import List, Tuple


# Method: DP, prev tower possiblity construction
# Time: O(n^2)
# Space: O(2^n)
# Not sure on space, every possible stacking ?


def can_add(bot: tuple, top: tuple) -> bool:
    return bot[0] > top[0] and bot[1] > top[1]


def get_circus_tower(arr: List[tuple]) -> List[tuple]:
    seqs = []  # Start poz -> list of heights
    sorted_arr = sorted(arr, reverse=True)

    # For every performer
    # (and every seq from prev performers,
    #  see if you can add them)
    for i in range(len(arr)):
        for good_seq in filter(lambda seq: can_add(seq[-1], sorted_arr[i]), seqs):
            good_seq.append(sorted_arr[i])

        # for j in range(len(seqs)):
        #     if can_add(seqs[j][-1], sorted_arr[i]):
        #         seqs[j].append(sorted_arr[i])
        seqs.append([sorted_arr[i]])
    return max(seqs, key=len)


if __name__ == "__main__":
    exs = [
        [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)],
    ]

    for perf_dim_arr in exs:
        print(
            f"Max tower is {get_circus_tower(perf_dim_arr)}"
            f" for performers {perf_dim_arr}"
        )
