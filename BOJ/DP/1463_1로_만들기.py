import sys

f = sys.stdin.readline
dp = [0 for i in range(10 ** 6 + 1)]
X = int(f())

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[X])
