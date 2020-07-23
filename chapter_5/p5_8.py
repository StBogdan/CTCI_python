from typing import List


def draw_line(screen: List[int],
              width_bits: int,
              x1: int,
              x2: int,
              y: int) -> None:
    # print(f"Putting line\t{x1} to {x2} on line {y}")
    w = width_bits // 8
    h = len(screen)//w

    start_index = w*y + x1//8
    end_index = w*y + x2//8

    # print(f"Indexes are\t{start_index} to {end_index}")

    start_mask = (0b1 << (8 - (x1 % 8))) - 1
    # print(f"Start mask is\t{start_mask:08b}")

    if start_index != end_index:
        screen[start_index] |= start_mask

        for i in range(start_index+1, end_index):
            screen[i] |= 0xFF

        end_mask = (0xFF << (8 - (x2 % 8))) % 256
        # print(f"End mask is\t{end_mask:08b}")

        screen[end_index] |= end_mask
    else:
        start_mask &= (0xFF) << (8 - x2 % 8)
        # print(f"Same mask is {start_mask:08b}")
        screen[start_index] |= start_mask


def print_screen(screen: List[int], width_bits: int):
    width = width_bits//8
    for i in range(len(screen)//width):
        for j in range(width):
            # print(f"{i} -- {j}")
            print(f"{screen[i*width+j]:08b}", end=" ")
        print()


if __name__ == "__main__":
    width_bits = 5 * 8
    h = 5
    screen = [0 for i in range(width_bits//8) for j in range(h)]
    # print_screen(screen, width_bits)
    for line_index in range(h):
        start_i = line_index + 1
        end_i = start_i*5
        draw_line(screen, width_bits, start_i, end_i, line_index)

    print_screen(screen, width_bits)
