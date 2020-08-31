
from collections import namedtuple
from typing import Tuple, Optional, List

Point = namedtuple("Point", "x y")


def get_line_eq(p1, p2):
    is_vertical = False
    slope =0
    if p1 == p2:
        raise Exception("Can't get a line eq for one point")

    if p1.x != p2.x:
        slope = (p1.y - p2.y) / (p1.x - p2.x)
        offset = p1.y - slope*p1.x
    else:  # Horiz line
        is_vertical = True
        offset = p1.x

    return (slope, offset, is_vertical)


def get_line_intersection(line_1, line_2):
    l1_slope, l1_offset, l1_vert = line_1
    l2_slope, l2_offset, l2_vert = line_2

    if (not (l1_vert or l2_vert)):
        if l1_slope == l2_slope and l2_offset != l1_offset:
            return None

        intersect_x = (l2_offset - l1_offset) / (l1_slope - l2_slope)
        intersect_y = intersect_x * l1_slope + l1_offset

        return Point(intersect_x, intersect_y)
    else:
        if l1_vert and l2_vert:
            if l1_offset != l2_offset:
                print("Got two verticals, but not at the same place")
                return None
            else:
                return (l1_offset, 0)  # Good as any
        else:
            vert_line_offset = l1_offset if l1_vert else l2_offset
            norm_line_slope, norm_line_offset = l2_slope, l2_offset if l1_vert else l1_slope, l1_offset

            isect_x = vert_line_offset
            isect_y = isect_x * norm_line_slope + norm_line_offset
            return Point(isect_x, isect_y)


def point_in_segment(p: Point, segment: Tuple[Point, Point]) -> bool:
    x_points = sorted([segment[0].x, segment[1].x])
    y_points = sorted([segment[0].y, segment[1].y])
    return x_points[0] <= p.x <= x_points[1]\
        and y_points[0] <= p.y <= y_points[1]


def check_line_overlap(s1, s2):
    if point_in_segment(s1[0], s2):
        return s1[0]
    elif point_in_segment(s1[1], s2):
        return s1[1]
    elif point_in_segment(s2[0], s1):
        return s2[0]
    elif point_in_segment(s2[1], s1):
        return s2[1]
    else:
        return None


def get_segment_insect(segment1: Tuple[Point, Point],
                       segment2: Tuple[Point, Point]) -> Optional[Point]:
    line_1 = get_line_eq(*segment1)
    line_2 = get_line_eq(*segment2)

    print(f"See {line_1} and {line_2}")

    if not line_1 or not line_2:
        print(f"Failed to determine a line from {line_1} and {line_2}")
    elif line_1 == line_2 or \
            ((line_1[2] and line_2[2]) and line_1[1] == line_2[1]):
        print(f"Got the same line twice, see {line_1} and {line_2}")
        return check_line_overlap(segment1, segment2)

    line_intersect = get_line_intersection(line_1, line_2)

    if line_intersect:
        if point_in_segment(line_intersect, segment1) \
                and point_in_segment(line_intersect, segment2):
            return line_intersect
        else:
            print(f"Point {line_intersect} not in both lines")


if __name__ == "__main__":
    exs = [
        ((Point(10, 10), Point(20, 20)), (Point(20, 10), Point(10, 20))),
        ((Point(10, 10), Point(10, 20)), (Point(10, 15), Point(10, 25))),
        ((Point(10, 10), Point(20, 10)), (Point(15, 10), Point(25, 10))),
        ((Point(10, 10), Point(10, 20)), (Point(15, 10), Point(15, 20))),
    ]

    for seg1, seg2 in exs:
        print(f"Meeting point of segments {seg1} and {seg2} "
              f"is {get_segment_insect(seg1,seg2)} ")
        print("-"*50)
