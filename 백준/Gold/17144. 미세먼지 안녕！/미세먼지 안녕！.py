"""
구현~
"""

import sys

f = sys.stdin.readline


dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def findPurifier(mat):
    pur = []
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == -1:
                pur.append([y, x])
            if len(pur) == 2:
                return pur


def diffusion(matOld, r, c, purifier):
    matNew = [[0 if [j, i] not in purifier else -1 for i in range(c)] for j in range(r)]

    for y in range(r):
        for x in range(c):
            # 확산X
            if matOld[y][x] == -1:
                continue
            if matOld[y][x] < 5:
                matNew[y][x] += matOld[y][x]
                continue

            # 확산량
            dust = matOld[y][x] // 5

            for dy, dx in dirs:
                ty, tx = y + dy, x + dx

                if 0 <= ty < r and 0 <= tx < c and matNew[ty][tx] != -1:
                    matOld[y][x] -= dust
                    matNew[ty][tx] += dust

            matNew[y][x] += matOld[y][x]

    return matNew


def airpurifier(mat, r, c, purifier):
    # 반시계 순환 --> 시계로 거슬러 올라감
    y, x = purifier[0]
    y -= 1
    while y > 0:
        mat[y][x] = mat[y - 1][x]
        y -= 1
    while x < c - 1:
        mat[y][x] = mat[y][x + 1]
        x += 1
    while y < purifier[0][0]:
        mat[y][x] = mat[y + 1][x]
        y += 1
    while x > 1:
        mat[y][x] = mat[y][x - 1]
        x -= 1
    mat[y][x] = 0

    # 시계 순환 --> 반시계로 거슬러 올라감
    y, x = purifier[1]
    y += 1
    while y < r - 1:
        mat[y][x] = mat[y + 1][x]
        y += 1
    while x < c - 1:
        mat[y][x] = mat[y][x + 1]
        x += 1
    while y > purifier[1][0]:
        mat[y][x] = mat[y - 1][x]
        y -= 1
    while x > 1:
        mat[y][x] = mat[y][x - 1]
        x -= 1
    mat[y][x] = 0

    return mat


if __name__ == "__main__":
    r, c, t = map(int, f().split())
    mat = [list(map(int, f().split())) for _ in range(r)]

    purifier = findPurifier(mat)

    for _ in range(t):
        mat = diffusion(mat, r, c, purifier)
        mat = airpurifier(mat, r, c, purifier)

    cnt = 0
    for _ in range(r):
        cnt += sum(mat[_])

    print(cnt+2)
