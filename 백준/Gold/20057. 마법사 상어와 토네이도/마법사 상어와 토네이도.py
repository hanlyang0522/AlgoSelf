"""
빡구현
"""

import sys
from collections import defaultdict

f = sys.stdin.readline

# 토네이도 이동방향
dirsTrnd = [[0, -1], [1, 0], [0, 1], [-1, 0]]
# 흩날린 모래 비율, y, x  / 상하는 yx 바꿔서
dirsFlow = [
    [1, -1, 1],
    [2, -2, 0],
    [7, -1, 0],
    [
        10,
        -1,
        -1,
    ],
    [5, 0, -2],
    [10, 1, -1],
    [7, 1, 0],
    [2, 2, 0],
    [1, 1, 1],
    [-1, 0, -1],
]


if __name__ == "__main__":
    n = int(f())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, f().split())))

    y, x = n // 2, n // 2  # 첫 위치
    di = 0  # 0123, ldru
    rFlag = False  # 방향 전환 결정
    rMax, rCnt = 1, 0
    overFlo = 0  # 빠져나간 모래

    while not (y == 0 and x == -1):
        # X --> Y 이동
        ty, tx = dirsTrnd[di][0], dirsTrnd[di][1]
        y, x = y + ty, x + tx

        ySand = mat[y][x]
        ySandOrigin = ySand
        mat[y][x] = 0
        for r, fy, fx in dirsFlow:
            # 방향에 맞게 변경
            if di == 1:
                fy, fx = -fx, fy
            elif di == 2:
                fx = -fx
            elif di == 3:
                fy, fx = fx, fy

            # 나머지는 전부 a로 가산
            if r == -1:
                if not (0 <= y + fy < n and 0 <= x + fx < n):
                    overFlo += ySand
                else:
                    mat[y + fy][x + fx] += ySand
                continue

            # 흩날린 모래 계산
            rSand = r * ySandOrigin // 100
            ySand -= rSand

            if not (0 <= y + fy < n and 0 <= x + fx < n):
                overFlo += rSand
            else:
                mat[y + fy][x + fx] += rSand

        # 방향 계산
        rCnt += 1
        if rCnt == rMax:
            if rFlag:
                rMax += 1
            di = (di + 1) % 4
            rFlag = not rFlag
            rCnt = 0

    print(overFlo)
