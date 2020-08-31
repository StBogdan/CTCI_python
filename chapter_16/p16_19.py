

from typing import List


def traverse_pond(matrix: List[List[int]], poz: tuple) -> int:
    x, y = poz
    n = len(matrix)
    m = len(matrix[0])

    pond_size = 1

    matrix[x][y] = -1

    # Look in all directions
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            new_x = x + dx
            new_y = y + dy

            # In in bounds, water and not visited, go there
            if 0 <= new_x < n and 0 <= new_y < m \
                    and matrix[new_x][new_y] == 0:
                pond_size += traverse_pond(matrix, (new_x, new_y))

    return pond_size


def find_pond_sizes(wet_map: List[List[int]]):
    pond_sizes = []
    for i in range(len(wet_map)):
        for j in range(len(wet_map[0])):
            if wet_map[i][j] == 0:
                pond_sizes.append(traverse_pond(wet_map, (i, j)))
    return pond_sizes


if __name__ == "__main__":
    ex_pond = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]

    print(f"In my map, pond sizes are: {find_pond_sizes(ex_pond)}")
