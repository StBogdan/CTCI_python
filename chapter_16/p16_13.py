from collections import namedtuple
from typing import List, Tuple

epsilon = 0.000001

Point = namedtuple("Point", "x y")


class Square:

    def __init__(self, topleft: Point, topright: Point, botleft: Point, botright: Point):
        self.top_left = topleft
        self.top_right = topright
        self.bot_left = botleft
        self.bot_right = botright

    def get_middle(self):
        return Point(
            (self.top_left.x + self.top_right.x) / 2,
            (self.top_left.y + self.bot_left.y) / 2)

    def __str__(self):
        return f"Square({self.top_left} to {self.bot_right})"


def get_line_from_points(p1: Point, p2: Point):
    is_vertical = False
    slope = 0
    if p1 == p2:
        raise Exception("Cannot get one line for 2 of the same point")

    if p1.x != p2.x:
        slope = (p1.y - p2.y) / (p1.x - p2.x)
        y_intercept = p1.y - slope * p1.x
    else:
        is_vertical = True
        y_intercept = p1.x  # Not acting as y_intercept

    return (slope, y_intercept, is_vertical)


def get_line_intersection(line1, line2):
    l1_slope, l1_offset, l1_vert = line1
    l2_slope, l2_offset, l2_vert = line2

    if (not (l1_vert or l2_vert)):
        if l1_slope == l2_slope and l2_offset != l1_offset:
            return None

        intersect_x = (l2_offset - l1_offset) / (l1_slope - l2_slope)
        intersect_y = intersect_x * l1_slope + l1_offset

        return Point(intersect_x, intersect_y)
    elif l1_vert and l2_vert:
        if l1_offset != l2_offset:
            print("Got two verticals, but not at the same place")
            return None
        else:
            return (l1_offset, 0)  # Good as any
    else:
        vline_x = l1_offset if l1_vert else l2_offset
        other_slope, other_offset, _ = line2 if l1_vert else line1

        isect_y = vline_x * other_slope + other_offset

        return Point(vline_x, isect_y)


def point_in_segment(p: Point, segment: Tuple[Point, Point]) -> bool:
    x_points = sorted([segment[0].x, segment[1].x])
    y_points = sorted([segment[0].y, segment[1].y])

    return x_points[0] - epsilon <= p.x <= x_points[1] + epsilon\
        and y_points[0] - epsilon <= p.y <= y_points[1] + epsilon


def get_intesection_points(sq: Square, mid_line: tuple) -> List[Point]:
    slope, offset, vertical = mid_line

    sides = ((sq.top_left, sq.top_right), (sq.top_left, sq.bot_left),
             (sq.bot_right, sq.bot_left), (sq.bot_right, sq.top_right))
    intercepts = []
    for sq_p1, sq_p2 in sides:
        side_line = get_line_from_points(sq_p1, sq_p2)
        intercept = get_line_intersection(side_line, mid_line)
        # print(f"Got possible intercept {intercept}")
        if point_in_segment(intercept, (sq_p1, sq_p2)):
            intercepts.append(intercept)

    return intercepts


def find_square_halving_line_points(s1: Square, s2: Square):
    # Returns the points at which the line splitting both squares into half,
    # Intersects the squares
    mid1 = s1.get_middle()
    mid2 = s2.get_middle()

    if mid1 == mid2:
        raise Exception("The two squares have the same middle point")

    mid_line = get_line_from_points(mid1, mid2)

    icept_points = get_intesection_points(
        s1, mid_line) + get_intesection_points(s2, mid_line)
    # print(icept_points)
    return max(icept_points), min(icept_points)


if __name__ == "__main__":
    exs = [
        (Square(Point(2, 5), Point(6, 5), Point(2, 1), Point(6, 1)),
         Square(Point(7, 8), Point(9, 8), Point(7, 6), Point(9, 6))),

        (Square(Point(2, 5), Point(6, 5), Point(2, 1), Point(6, 1)),
         Square(Point(5, 3), Point(6, 3), Point(5, 2), Point(6, 2))),
    ]

    for sq1, sq2 in exs:
        print(f"For the squares {sq1} and {sq2},"
              f" the mid line has intersections {find_square_halving_line_points(sq1, sq2)}"
              f" same as {find_square_halving_line_points(sq2, sq1)}")
        print("-"*50)
