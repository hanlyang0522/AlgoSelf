# 1. dp를 list로 만들어 (개수, 방향)을 저장
# --> 방향별로 dp1,2,3을 따로 만듬!
import sys

f = sys.stdin.readline


def move(n, li):
    dp = [[[0] * 3 for _ in range(n)] for __ in range(n)]
    dp[0][1][0] = 1  # [y][x][n] 순서, n=가로, 세로, 대각선

    for i in range(2, n):
        if li[0][i] == 0:
            dp[0][i][0] = dp[0][i - 1][0]

    for y in range(1, n):
        for x in range(1, n):
            if li[y][x] == 0:
                dp[y][x][0] = dp[y][x - 1][0] + dp[y][x - 1][2]  # 가로 = x-1의 가로 + 대각선
                dp[y][x][1] = dp[y - 1][x][1] + dp[y - 1][x][2]  # 세로 = y-1의 세로 + 대각선

            if li[y][x] == 0 and li[y - 1][x] == 0 and li[y][x - 1] == 0:
                dp[y][x][2] = dp[y - 1][x - 1][0] + dp[y - 1][x - 1][1] + dp[y - 1][x - 1][2]

    print(sum(dp[-1][-1]))
    # for i in range(n):
    #     print(dp[i])


if __name__ == "__main__":
    n = int(f())
    li = []
    for i in range(n):
        li.append(list(map(int, f().split())))

    move(n, li)
