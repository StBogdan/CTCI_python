def shift_lockers(n:int):
    locker_status = [False] *n
    for i in range(n):
        for j in range(i, n, i+1):
            locker_status[j] = not locker_status[j]

    # print(locker_status)
    for i in range(n):
        if locker_status[i]:
            print(f"Locker {i+1} still open")

if __name__ == "__main__":
    shift_lockers(100)