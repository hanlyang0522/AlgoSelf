"""
- bfs
1. 고슴도치 이동
2. 물 이동 -> 고슴도치면 덮어씌움
"""

import sys
from collections import deque

f = sys.stdin.readline

global jido, dist, dq

dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]


def solve(by, bx):
    while dq:
        y, x = dq.popleft()

        if jido[by][bx] == "S":  # 비버집 도착하면 return
            return dist[by][bx]

        for dy, dx in dirs:
            ty, tx = y + dy, x + dx

            if ty < 0 or ty >= r or tx < 0 or tx >= c:
                continue

            # 고슴도치 이동
            if jido[y][x] == "S" and (jido[ty][tx] == "." or jido[ty][tx] == "D"):
                jido[ty][tx] = "S"
                dist[ty][tx] = dist[y][x] + 1
                dq.append([ty, tx])

            # 물 이동. 고슴도치는 덮어씌움
            elif jido[y][x] == "*" and (jido[ty][tx] == "." or jido[ty][tx] == "S"):
                jido[ty][tx] = "*"
                dq.append([ty, tx])

    return "KAKTUS"


if __name__ == "__main__":
    r, c = map(int, f().split())

    dist = [[0] * c for _ in range(r)]
    jido = [list(f().strip()) for _ in range(r)]
    dq = deque()
    by, bx = -1, -1

    for y in range(r):
        for x in range(c):
            if jido[y][x] == "S":
                dq.append([y, x])
            elif jido[y][x] == "D":
                by, bx = y, x

    for y in range(r):
        for x in range(c):
            if jido[y][x] == "*":  # 물은 나중에 이동
                dq.append([y, x])

    print(solve(by, bx))
