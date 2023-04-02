"""
x: 0 ~ 17
y: 1 ~ 18
d1, d2: 최대 20*20 미만
선거구: 최대 20*20
--> 18 * 18 * 400 * 400 ~= 6.4 * 10^7
"""

import sys

f = sys.stdin.readline


def solve(row, col, d1, d2):

    # 선거구 1
    n1 = 0
    col1 = y + 1
    for r in range(row + d1):
        if r >= row:
            col1 -= 1
        n1 += sum(mat[r][:col1])

    # 2
    n2 = 0
    col2 = col + 1
    for r in range(row + d2 + 1):
        if r > row:
            col2 += 1
        n2 += sum(mat[r][col2:])

    # 3
    n3 = 0
    col3 = col - d1
    for r in range(row + d1, N):
        n3 += sum(mat[r][:col3])
        if r < row + d1 + d2:
            col3 += 1

    # 4
    n4 = 0
    col4 = col + d2 - N
    for r in range(row + d2 + 1, N):
        n4 += sum(mat[r][col4:])
        if r <= row + d1 + d2:
            col4 -= 1

    # 5
    n5 = total - sum([n1, n2, n3, n4])

    return max(n1, n2, n3, n4, n5) - min(n1, n2, n3, n4, n5)


if __name__ == "__main__":
    N = int(f())
    mat = [list(map(int, f().split())) for _ in range(N)]

    ans = 100 * N * N
    total = 0
    for _ in range(N):
        total += sum(mat[_])

    for x in range(N - 2):
        for y in range(1, N - 1):
            for d1 in range(1, N - 1):
                for d2 in range(1, N - 1):
                    if x + d1 + d2 > N or y - d1 < 0 or y + d2 > N:
                        continue
                    ans = min(ans, solve(x, y, d1, d2))

    print(ans)
