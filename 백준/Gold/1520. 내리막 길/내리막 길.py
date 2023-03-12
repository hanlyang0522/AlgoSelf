"""

"""


import sys
from collections import deque


f = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(sy, sx):
    if sy == m - 1 and sx == n - 1:
        return 1

    if dp[sy][sx] != -1:
        return dp[sy][sx]

    cnt = 0
    for dy, dx in dirs:
        ty, tx = sy + dy, sx + dx

        if 0 <= ty < m and 0 <= tx < n and mat[sy][sx] > mat[ty][tx]:
            cnt += dfs(ty, tx)

    dp[sy][sx] = cnt
    return dp[sy][sx]


if __name__ == "__main__":
    global mat

    m, n = map(int, f().split())
    mat = [(list(map(int, f().split()))) for _ in range(m)]

    dp = [[-1 for _ in range(n)] for __ in range(m)]
    print(dfs(0, 0))
