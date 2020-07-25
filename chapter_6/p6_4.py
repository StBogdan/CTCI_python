
def ants_collision_chance(num_vertex: int):
    # Ants not going the same way => 2 options (either left of right)
    # Ants are equally likely to go either way
    good_cases =2
    all_cases = 2**num_vertex

    return (all_cases - good_cases)/ all_cases   


if __name__ == "__main__":
    for i in range(3,10):
        print(f"Chance of ant collision on {i}-vertex polygon"
              f" is {ants_collision_chance(i):10}, compared with {1- (1/2)**(i-1):10}")