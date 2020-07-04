from typing import List


def rec_prn_builder(left2p, to_close):
    if left2p == 0:
        return [[]]

    res = []
    if to_close > 0:
        sub_res = rec_prn_builder(left2p - 1, to_close-1)
        res.extend([[")"] + sub_r for sub_r in sub_res])

    if to_close < left2p:
        sub_res = rec_prn_builder(left2p-1, to_close+1)

        res.extend([["("] + sub_r for sub_r in sub_res])

    return res


def pair_builder(pairs: int) -> List[str]:
    res_lists = rec_prn_builder(pairs*2, 0)
    return ["".join(res_list) for res_list in res_lists]


if __name__ == "__main__":
    print(pair_builder(1))
