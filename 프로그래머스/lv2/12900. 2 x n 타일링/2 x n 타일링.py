def solution(n):
    dp = [-1] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 1000000007

    return dp[n]