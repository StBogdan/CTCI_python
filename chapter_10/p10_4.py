class Listy:
    def __init__(self, arr):
        self.arr = arr

    def elemAt(self, index: int):
        return self.arr[index] if index < len(self.arr) else -1

def search_unsized_list(arr: Listy, target: int) -> int:
    # Lenght is not known
    ind = 0
    low = 0
    while arr.elemAt(ind) != -1 and arr.elemAt(ind) <= target:
        ce = arr.elemAt(ind)
        low = ind
        if not ind:
            ind = 1
        else:
            ind *= 2

    high = ind
    while low <= high:
        # print(f"Looking at low and high {low} and {high}")
        mid = (low + high) // 2
        ce = arr.elemAt(mid)
        if ce == target:
            return mid
        elif ce == -1 or ce > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    exs = [([1, 2, 3, 4, 5, 6, 7, 8], 10),
           ([12, 13, 14, 15], 15),
           (list(range(62)), 61)]
    for arr, target in exs:
        listy_arr = Listy(arr)
        print(
            f"Looking for {target} in {arr}, found location ?"
            f" {search_unsized_list(listy_arr, target)}")
