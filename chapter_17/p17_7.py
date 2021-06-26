from typing import Tuple, List
from utils.graphs import Vertex


# Method: Build graph, DFS
# Time: O(V + E)
# Space: O(V + E)
# Notes:    V = vertexes, nr of names
#           E = edges, nr of name equivalencies


def get_truename_occurences(
    names_list: List[tuple], name_pairs: List[tuple]
) -> List[tuple]:
    name_dict = {name: Vertex((name, occ)) for name, occ in names_list}

    # Build graph
    for name1, name2 in name_pairs:
        if name1 not in name_dict or name2 not in name_dict:
            continue
        name_dict[name1].edges.add(name_dict[name2])
        name_dict[name2].edges.add(name_dict[name1])

    seen_nodes = set()
    name_totals = {}

    # DFS on the other names
    for name, name_vertex in name_dict.items():
        if name in seen_nodes:
            continue
        name_totals[name] = traverse_connected_names(name_vertex, seen_nodes)

    return list(name_totals.items())


def traverse_connected_names(vertex: Vertex, seen: set) -> int:
    name, occ = vertex.val
    if name in seen:
        return 0

    seen.add(name)
    extra_sum = sum(traverse_connected_names(child, seen) for child in vertex.edges)
    return occ + extra_sum


if __name__ == "__main__":
    ex_names = [
        ("John", 15),
        ("Jon", 12),
        ("Chris", 13),
        ("Kris", 4),
        ("Christopher", 19),
    ]
    ex_pairs = [
        ("John", "Jon"),
        ("John", "Johny"),
        ("Chris", "Kris"),
        ("Chris", "Christopher"),
    ]

    print(f"True counts are {get_truename_occurences(ex_names, ex_pairs)}")
