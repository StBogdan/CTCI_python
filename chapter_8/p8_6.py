def hanoi_towers(n):
    stacks = [[], [], []]
    stacks[0] = list(range(n, 0, -1))

    print(f"Got start stacks\t{stacks}")
    move_stack(n, 0, 2, stacks)
    display_stacks(stacks)


def move_disk(source_ind, target_ind, stacks):
    stacks[target_ind].append(stacks[source_ind].pop())


def display_stacks(stacks):
    for i, stack in enumerate(stacks):
        print(f"{i} -> {stack}")
    print("-"*50)


def move_stack(elem_bot, src, target, stacks):
    display_stacks(stacks)
    temp_stack = 3 - src - target
    top_src = stacks[src][-1]
    if top_src == elem_bot:
        move_disk(src, target, stacks)
    else:
        move_stack(elem_bot-1, src, temp_stack, stacks)
        move_disk(src, target, stacks)
        move_stack(elem_bot-1, temp_stack, target, stacks)


if __name__ == "__main__":
    hanoi_towers(4)
