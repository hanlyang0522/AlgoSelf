"""
- bfs

"""

import sys
from collections import deque

f = sys.stdin.readline


global cMap, r, c

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # y,x


def printcMap():
    for y in range(len(cMap)):
        for x in range(len(cMap[0])):
            print(cMap[y][x], end=" ")
        print("")


def bfs():
    cheeseCnt = 0
    visited = [[0] * c for _ in range(r)]

    dq = deque([[0, 0]])
    visited[0][0] = 1

    while dq:
        y, x = dq.popleft()

        for dy, dx in dirs:
            ty, tx = y + dy, x + dx

            if ty < 0 or ty >= r or tx < 0 or tx >= c:
                continue

            if visited[ty][tx]:
                continue

            if cMap[ty][tx] == 0:
                visited[ty][tx] = 1
                dq.append([ty, tx])
            else:
                visited[ty][tx] = 1
                cMap[ty][tx] = 0
                cheeseCnt += 1

    return cheeseCnt


def solve(cCnt):
    time = 0
    cCntPrev = cCnt

    while cCnt > 0:
        if cCnt < 0:
            print("error")

        time += 1
        cCntPrev = cCnt
        cCnt -= bfs()

    print(time)
    print(cCntPrev)

    return -1


if __name__ == "__main__":
    r, c = map(int, f().split())

    cMap = []
    cCnt = 0

    for i in range(r):
        tmp = list(map(int, f().split()))

        cCnt += tmp.count(1)
        cMap.append(tmp)

    solve(cCnt)
