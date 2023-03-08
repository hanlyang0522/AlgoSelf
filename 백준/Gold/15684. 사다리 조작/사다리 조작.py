"""
구현
"""


import sys
from itertools import combinations

f = sys.stdin.readline


def isLine(y, x):
    """
    가로선 (y,x)랑 겹치거나 연속되는지 확인
    """
    for dx in [-1, 0, 1]:
        tx = x + dx
        if 0 <= tx < n - 1 and matOri[y][tx] == 1:
            return True

    return False


def isOk(mat):
    width = len(mat[0])

    for x in range(width + 1):
        idx = x

        for y in range(len(mat)):
            # 좌로 이동
            if idx > 0 and mat[y][idx - 1] == 1:
                idx -= 1
            # 우로 이동
            elif idx < width and mat[y][idx]:
                idx += 1

        if idx != x:
            return False

    return True


if __name__ == "__main__":
    n, m, h = map(int, f().split())  # 세로선, (총)가로선, 점선

    matOri = [[0 for _ in range(n - 1)] for __ in range(h)]
    for _ in range(m):
        y, x = map(int, f().split())
        matOri[y - 1][x - 1] = 1

    combis = []
    for i in range(4):
        combis += list(combinations(range(h * (n - 1)), i))

    for comb in combis:
        mat = [m[:] for m in matOri]

        # 가로선 1개 추가
        if len(comb) == 1:
            y1, x1 = comb[0] // (n - 1), comb[0] % (n - 1)

            if isLine(y1, x1):
                continue
            mat[y1][x1] = 1

        # 가로선 2개 추가
        elif len(comb) == 2:
            y1, x1 = comb[0] // (n - 1), comb[0] % (n - 1)
            y2, x2 = comb[1] // (n - 1), comb[1] % (n - 1)

            if isLine(y1, x1) or isLine(y2, x2):
                continue
            mat[y1][x1] = 1
            mat[y2][x2] = 1

        elif len(comb) == 3:
            y1, x1 = comb[0] // (n - 1), comb[0] % (n - 1)
            y2, x2 = comb[1] // (n - 1), comb[1] % (n - 1)
            y3, x3 = comb[2] // (n - 1), comb[2] % (n - 1)

            if isLine(y1, x1) or isLine(y2, x2) or isLine(y3, x3):
                continue
            mat[y1][x1] = 1
            mat[y2][x2] = 1
            mat[y3][x3] = 1

        if isOk(mat):
            print(len(comb))
            exit()

    print(-1)
