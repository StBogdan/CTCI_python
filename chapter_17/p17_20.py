import heapq as hq


class MedianHolder:

    def __init__(self):
        self.left_heap = [] # Max (on top) heap
        self.right_heap = [] # Min (on top) heap
        self.size = 0

    def add_elem(self, x: int):

        if self.left_heap and x > -self.left_heap[0]:
            hq.heappush(self.right_heap, x)
        else:
            hq.heappush(self.left_heap, -x)

        if len(self.left_heap) < len(self.right_heap):  # Too much on right
            hq.heappush(self.left_heap, - hq.heappop(self.right_heap))
        elif len(self.left_heap) > len(self.right_heap) + 1:  # Too much on left
            hq.heappush(self.right_heap, -hq.heappop(self.left_heap))

        self.size += 1

    def get_median(self):
        if self.size == 0:
            raise Exception("No elems")
        if self.size % 2 == 0:
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return -self.left_heap[0]


if __name__ == "__main__":
    mh = MedianHolder()
    for i in range(25):
        mh.add_elem(i)
        print(f"At elem {i}\t, Median is now {mh.get_median()} ")
