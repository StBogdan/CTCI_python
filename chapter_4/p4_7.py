

from utils.graphs import Ditex
from collections import OrderedDict, defaultdict
from typing import List

# TODO Redo as topological sort


def build_nodes(projects: List[chr], deps: List[tuple]):
    nodes = {x: Ditex(x) for x in projects}

    for (a, b) in deps:
        # print(f"Looking at tuple {a} and {b}")
        nodes[b].out_edges.add(nodes[a])
        nodes[a].in_edges.add(nodes[b])

    sn = OrderedDict()
    seen_count = len(sn)-1
    while seen_count != len(sn):  # Check progress
        seen_count = len(sn)

        for key, node in nodes.items():
            if not {edge.val for edge in node.out_edges} - sn.keys():
                sn[node.val] = 1
                down_build(node, sn)
            else:
                print(f"node {key} is waiting on {[x.val for x in node.out_edges]}, "
                      f" seen so far {list(sn.keys())}")

    if len(sn) == len(projects):
        return list(sn.keys())
    else:
        raise Exception("No valid build")


def down_build(node: Ditex, seen: dict):
    for nodes_child in node.in_edges:
        if not nodes_child.out_edges - seen.keys():
            print(
                f"Adding {nodes_child.val} as out_edges are \
                    {[x.val for x in nodes_child.out_edges]},\t \
                        compared to seen {list(seen.keys())}")
            seen[nodes_child.val] = 1
            down_build(nodes_child, seen)


if __name__ == "__main__":
    # projects = ['a', 'b', 'c', 'd', 'e', 'f']
    # deps = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    projects = ['a', 'b', 'c']
    deps = [('c', 'a')]
    build_order = build_nodes(projects, deps)
    print(f"Build order is {build_order}")
