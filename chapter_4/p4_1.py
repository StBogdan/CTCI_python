from typing import List
from utils.graphs import Ditex
from collections import deque


def populate_graph(edges: List[tuple]) -> dict:
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = Ditex(a)
        if b not in graph:
            graph[b] = Ditex(b)

        graph[a].out_edges.add(b)
        graph[b].in_edges.add(a)
    return graph


def route_digraph(edges: List[tuple], s: int, e: int):
    graph = populate_graph(edges)
    start_dq = deque()
    end_dq = deque()

    seen_start = set([s])
    seen_end = set([e])

    start_dq.append(s)
    end_dq.append(e)

    round_robin_flag = True

    while start_dq and end_dq:
        if round_robin_flag:  # From start to end
            ce = graph[start_dq.popleft()]
            seen_start.add(ce.val)

            if ce.val in seen_end:
                return True
            for child in ce.out_edges:
                if child not in seen_start:
                    start_dq.append(child)
        else:  # From end toward start
            ce = graph[end_dq.popleft()]
            seen_end.add(ce.val)

            if ce.val in seen_start:
                return True

            for parent in ce.in_edges:
                if parent not in seen_end:
                    end_dq.append(parent)

        round_robin_flag != round_robin_flag
    return False


if __name__ == "__main__":
    edges = [(1, 11), (1, 12), (1, 14), (12, 23),
             (23, 2), (2, 21), (2, 22), (24, 2)]
    targets = (1, 2), (11, 24), (1, 22), (1, 11)
    for s, e in targets:
        print(
            f"Is there a route from {s} to {e} ? {route_digraph(edges, s,e)}")
