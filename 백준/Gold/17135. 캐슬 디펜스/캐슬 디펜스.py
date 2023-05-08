"""
구현
15c3 = 455 (최대 경우의 수) * 15줄 = 6825

"""

import sys
from copy import deepcopy
from itertools import combinations


f = sys.stdin.readline


def isEmpty():
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                return False
    return True


def attack(comb):
    attackLi = []
    count = 0

    for x in comb:  # 각 궁수별 가능 타겟
        pos = []

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:  # 가능 타겟 저장
                    dist = abs(i - n) + abs(j - x)
                    if d >= dist:
                        pos.append((dist, i, j))

        pos.sort(key=lambda x: (x[0], x[2]))  # 가깝고, 왼쪽순 정렬
        if pos:
            attackLi.append(pos[0])

    # 타겟 제거
    for _, i, j in attackLi:
        if mat[i][j] == 1:
            mat[i][j] = 0
            count += 1

    return count


def move():
    # 1칸씩 내려옴
    for i in range(-1, -n, -1):
        mat[i] = mat[i - 1]
    mat[0] = [0] * m


if __name__ == "__main__":
    global _mat

    n, m, d = map(int, f().split())
    _mat = [list(map(int, f().split())) for _ in range(n)]
    result = -1

    for comb in combinations([i for i in range(m)], 3):
        mat = deepcopy(_mat)
        cnt = 0

        while not isEmpty():
            cnt += attack(comb)
            move()
        result = max(result, cnt)

    print(result)
