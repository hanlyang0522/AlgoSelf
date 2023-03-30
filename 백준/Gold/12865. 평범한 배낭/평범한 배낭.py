"""
"Well-known"
"""

import sys

f = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, f().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for y in range(1, n + 1):
        weight, val = map(int, f().split())

        for x in range(1, k + 1):
            if x < weight:
                dp[y][x] = dp[y - 1][x]
            else:
                dp[y][x] = max(dp[y - 1][x - weight] + val, dp[y - 1][x])

    print(dp[-1][-1])
