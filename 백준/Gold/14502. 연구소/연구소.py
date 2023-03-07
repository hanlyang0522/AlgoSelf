import sys
from itertools import combinations
from copy import deepcopy
from collections import deque


f = sys.stdin.readline

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(mat, virus):
    q = deque(virus)
    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            ty, tx = y + dy, x + dx

            if 0 <= ty < n and 0 <= tx < m and mat[ty][tx] == 0:
                mat[ty][tx] = 2
                q.append([ty, tx])

    cnt = 0
    for y in range(n):
        for x in range(m):
            if mat[y][x] == 0:
                cnt += 1

    return cnt


if __name__ == "__main__":
    n, m = map(int, f().split())
    _mat = []
    for _ in range(n):
        _mat.append(list(map(int, f().split())))

    virus = []
    notSafe = 0
    for y in range(n):
        for x in range(m):
            if _mat[y][x] == 2:
                virus.append([y, x])

    cnt = 0
    for w1, w2, w3 in combinations(range(n * m), 3):
        y1, x1 = w1 // m, w1 % m
        y2, x2 = w2 // m, w2 % m
        y3, x3 = w3 // m, w3 % m

        mat = deepcopy(_mat)
        if mat[y1][x1] != 0 or mat[y2][x2] != 0 or mat[y3][x3] != 0:
            continue

        mat[y1][x1] = mat[y2][x2] = mat[y3][x3] = 1
        cnt = max(cnt, bfs(mat, virus))

    print(cnt)
