def triple_step(n: int) -> int:

    dp = [1, 1, 2]

    if n < 3:
        return dp[n]

    for i in range(3, n+1):
        new_elem = sum(dp)
        dp[0] = dp[1]
        dp[1] = dp[2]
        dp[2] = new_elem

    return dp[2]


if __name__ == "__main__":
    for i in range(20):
        print(f"Going to {i} step, ways to do this: {triple_step(i)}")
