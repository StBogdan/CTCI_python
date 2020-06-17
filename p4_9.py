# BST Sequences


def rec_weave(l1, l2, atm_ans):
    lol = []
    if l1:
        rest_of_lists = rec_weave(l1[1:], l2, atm_ans + [l1[0]])
        lol.extend(rest_of_lists)
    else:
        return [atm_ans + l2]

    if l2:
        rest_of_lists_2 = rec_weave(l1, l2[1:], atm_ans + [l2[0]])
        lol.extend(rest_of_lists_2)
    else:
        return [atm_ans + l1]

    return lol

# [1,2]
# [3,4]
# Result: [1,2,3,4], [3,4,1,2], and others


def weave(l1, l2):
    return rec_weave(l1, l2, [])
    # l1 [1]
    # l2 [2]
    # [2,1 ], [1,2]


if __name__ == "__main__":
    print("Result")
    # print(weave([1], [2]))
    print(weave([1], [3, 5, 4]))
