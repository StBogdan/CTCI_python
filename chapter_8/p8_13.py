from functools import lru_cache
from collections import namedtuple
from typing import List

Box = namedtuple("Box", "w l h")


def can_stack(bot: Box, top: Box):
    return bot.w > top.w and bot.l > top.l and bot.h > top.h


def max_box_stack(boxes: List[Box]):
    # Need to be immutable for the cache
    sort_boxes = tuple(sorted(boxes, key=lambda box: -box.h))
    # print(f"Sorted boxes are {sort_boxes}")

    box_stack_sizes = [stack_boxes(sort_boxes, i)
                       for i in range(len(sort_boxes))]
    return max(box_stack_sizes)


@lru_cache(None)
def stack_boxes(boxes: List[Box], box_index: int) -> int:
    height_of_boxpile = 0
    box_now = boxes[box_index]

    max_h_added = 0

    for i in range(box_index+1, len(boxes)):
        h_added = 0
        if can_stack(box_now, boxes[i]):
            h_added = stack_boxes(boxes, i)
            max_h_added = max(max_h_added, h_added)

    height_of_boxpile = box_now.h + max_h_added
    return height_of_boxpile


if __name__ == "__main__":
    boxes = [
        Box(20, 20, 20),
        Box(10, 10, 10),
        Box(5, 5, 5),
        Box(30, 5, 30),
        Box(15, 15, 15)]
    print(f"Maximum height for boxes is {max_box_stack(boxes)}")
