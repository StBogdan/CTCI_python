from copy import copy
from typing import List
import heapq


def smallest_k_elem(arr: List[int], k: int) -> List[int]:
    heap = []

    for i in range(k):
        heapq.heappush(heap, -arr[i])

    for i in range(k+1, len(arr)):
        if arr[i] < -heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -arr[i])

    return [-x for x in heap]


if __name__ == "__main__":
    exs = [
        ([1, 2, 3, 4, 5, 6], 4),
        ([1, 2, 2, 2, 1, 1, 0], 3)
    ]

    for ex, k in exs:
        print(f"{k} smalles in {ex} are {smallest_k_elem(ex,k)}")
