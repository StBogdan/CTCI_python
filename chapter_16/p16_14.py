
from typing import List, Tuple
from collections import defaultdict, namedtuple
import math

Point = namedtuple("Point", "x y")


def get_line_eq(p1, p2):
    is_vertical = False
    if p1.x == p2.x and p1.y == p2.y:
        raise Exception("Can't get a line for one point")

    y_diff = p1.y - p2.y
    x_diff = p1.x - p2.x
    slope = None

    if y_diff == 0:  # Horiz line
        slope = 0
        offset = p1.y
    elif x_diff == 0:
        is_vertical = True
        offset = p1.x
    else:
        slope = x_diff / y_diff
        offset = p1.y - slope * p1.x

    return slope, offset, is_vertical


def get_most_popular_line(lines: dict, epsilon: float) -> Tuple[tuple, int]:
    lines_list = list(lines.keys())
    lines_len = len(lines_list)

    # Check every pair of lines 
    # #for differences within the epsilon threshold
    for i in range(lines_len-1):
        for j in range(i+1, lines_len):
            l1_slope, l1_offset, l1_vertical = lines_list[i]
            l2_slope, l2_offset, l2_vertical = lines_list[j]

            offset_is_close = math.isclose(
                l1_offset, l2_offset, abs_tol=epsilon)

            if l1_vertical != l2_vertical:
                continue
            elif l1_vertical == l2_vertical and l2_vertical:
                if offset_is_close:
                    lines[lines_list[i]] += lines[lines_list[j]]
            else:
                if math.isclose(l1_slope, l2_slope, abs_tol=epsilon) and \
                        offset_is_close:
                    lines[lines_list[i]] += lines[lines_list[j]]
    return max(lines.items(), key=lambda x: x[1])


def find_line_with_most_points(points: List[Point]) -> tuple:
    line_occ_dict = defaultdict(int)
    epsilon = 0.0001

    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            if points[i] == points[j]:
                continue

            line_now = get_line_eq(points[i], points[j])
            line_occ_dict[line_now] += 1

    return get_most_popular_line(line_occ_dict, epsilon)


if __name__ == "__main__":
    exs = [
        [Point(1, 1), Point(4, 1), Point(8, 3),
         Point(3, 3), Point(1, 5), Point(2, 2), Point(4, 7)],
        [Point(10, 15), Point(10, 16),
         Point(10, 17), Point(11, 15), Point(12, 12)],
    ]

    for ex in exs:
        line, point_count = find_line_with_most_points(ex)
        print(f"Line with max points is {line}, with {point_count} points")
