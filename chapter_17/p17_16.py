from typing import List


def masseuse_sched(appointments: List[int]):
    n = len(appointments)

    dp = [0 for _ in range(n+3)]
    cmax = 0

    for i in range(n-1, -1, -1):
        dp[i] = appointments[i] + max(dp[i+2], dp[i+3])
        if dp[i] > cmax:
            cmax = dp[i]

    return max(dp[0], dp[1])


if __name__ == "__main__":
    exs = [
        [30, 15, 60, 75, 45, 15, 15, 45],
        [150, 30, 45, 60, 75, 150]
    ]

    for ex in exs:
        print(f"Max mins is {masseuse_sched(ex)} for bookings {ex}")
