from typing import List


def diving_board_lengths(k: int, longer: int, shorter: int) -> List[int]:
    len_now = shorter * k
    ans = [len_now]

    if shorter == longer:
        return ans

    for i in range(k):
        len_now += longer - shorter
        ans.append(len_now)

    return ans


if __name__ == "__main__":
    exs = [[10, 10, 5], [10, 10, 10], [10, 1, 2]]
    for k, longer, shorter in exs:
        print(f"Ways to measure {k} planks"
              f" from {longer} and {shorter}"
              f" are: {diving_board_lengths(k,longer,shorter)} ")
