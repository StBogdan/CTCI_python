from typing import List


def gen_subsets(set_elems: List[int], offset: int):
    if offset == len(set_elems) - 1:
        return [[set_elems[offset]], []]

    wo_elem = gen_subsets(set_elems, offset+1)
    w_elem = [[set_elems[offset]] +
              subset for subset in gen_subsets(set_elems, offset+1)]
    return w_elem + wo_elem


if __name__ == "__main__":
    exs = [
        [1, 2, 3],
        [1],
        [1, 2, 3, 4]
    ]

    for arr in exs:
        subsets = gen_subsets(arr, 0)
        print(f"Subsets of {arr} are size {len(subsets)}:  {subsets}")
