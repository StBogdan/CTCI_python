import random

def sim_children(pop_size: int):
    boys = 0
    girls = 0
    while pop_size:
        more_children_couples =0
        for i in range(pop_size):
            has_girl = bool(random.getrandbits(1))
            if not has_girl:
                boys += 1
                more_children_couples += 1
            else:
                girls += 1
        pop_size = more_children_couples

    return boys, girls


if __name__ == "__main__":
    for i in range(1, 8):
        pop_boys, pop_girls = sim_children(10**i)
        print(f"For pop size {10**i:10}\t, ratio {pop_boys/pop_girls:10}\t, got boys {pop_boys}\t girls {pop_girls}")
