import sys

f = sys.stdin.readline

N, M = map(int, f().split())
li = list(map(int, f().split()))
dp = [li[0]]

for num in li:
    dp.append(num + dp[-1])

for _ in range(M):
    i, j = map(int, f().split())
    print(dp[j] - dp[i - 1])

# 메모리 초과!
# dp = [[0] * i for i in range(1, N + 1)]
# dp[0][0] = li[0]

# for i in range(1, N):
#     for j in range(i):
#         dp[i][j] = dp[i - 1][j] + li[i]
#     dp[i][i] = li[i]

# for _ in range(M):
#     i, j = map(int, f().split())
#     print(dp[j - 1][i - 1])
