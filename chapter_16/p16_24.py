def old_2sum(arr, target):
    seen = {}
    ans = []
    for i, x in enumerate(arr):
        if target - x in seen:
            ans.append((arr[i], arr[seen[target-x]]))
        else:
            seen[x] = i

    return ans


if __name__ == "__main__":
    exs = [([4, 6, 10, 15, 16], 21),
           ([12, 6, 7, 1, 19, 3, 0, 4, 40], 7),
           ([4, 4, 4, 2, 2, 1, 1, 1, 1, 3], 4)]
    for arr, x in exs:
        print(f"Pairs for targeet {x} in {arr} are {old_2sum(arr,x)}")
