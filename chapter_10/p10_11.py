from typing import List

def peaks_and_valeys(arr: List[int]) -> List[int]:
    for i in range(len(arr)-2):
        # print(f"looking at {arr[i:i+3]}")
        if arr[i] >= arr[i+1]:
            if arr[i+2] < arr[i+1]:
                arr[i+1], arr[i+2] = arr[i+2], arr[i+1]
        else:
            if arr[i+1] < arr[i+2]:
                arr[i+1], arr[i+2] = arr[i+2], arr[i+1]
    return arr

if __name__ == "__main__":
    exs = [[1,2,4,5,6,7], [7,6,5,4,3,2,1], [9,10,4,8,7]]
    for ex in exs:
        print(f"Peaked arr {ex}\tis\t{peaks_and_valeys(ex)}")