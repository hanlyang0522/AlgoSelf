"""
구현
1. 단순히 모든 block에서 bfs를 하니까 기준 block을 못 찾는 문제가 발생..
"""


import sys
from collections import deque

f = sys.stdin.readline

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # ldru


def findGroup(y, x, idx):
    q = deque()
    q.append([y, x])

    blocks = [[y, x]]
    rainbows = []

    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            ty, tx = y + dy, x + dx

            if 0 <= ty < n and 0 <= tx < n:
                # 무지개
                if mat[ty][tx] == 0 and not visit[ty][tx]:
                    q.append([ty, tx])
                    rainbows.append([ty, tx])
                    visit[ty][tx] = 1
                elif mat[ty][tx] == idx and not visit[ty][tx]:
                    q.append([ty, tx])
                    blocks.append([ty, tx])
                    visit[ty][tx] = 1

    # 무지개는 다른 그룹도 사용 가능
    for y, x in rainbows:
        visit[y][x] = 0

    return [len(blocks + rainbows), len(rainbows), blocks + rainbows]


def removeGroup(group):
    for y, x in group[2]:
        mat[y][x] = -2

    return group[0] ** 2


def gravity():
    for x in range(n):
        d, u = n - 1, n - 1

        while u >= 0:
            # 비어있을 경우 u가 1칸 올라감
            if mat[u][x] == -2:
                u -= 1
            # u가 검은 블록 만나면 d 갱신 필요
            elif mat[u][x] == -1:
                d = u - 1
                u -= 1
            # 일반 블록은 아래로
            else:
                if u != d:
                    mat[d][x] = mat[u][x]
                    mat[u][x] = -2
                d -= 1
                u -= 1


def rotate():
    global mat
    matNew = [[-2 for _ in range(n)] for __ in range(n)]

    for y in range(n):
        for x in range(n):
            matNew[y][x] = mat[x][n - 1 - y]

    mat = matNew[:]


def autoPlay():
    global visit
    score = 0

    while True:
        # 블록 그룹 탐색
        visit = [[0 for _ in range(n)] for __ in range(n)]
        groups = []

        for y in range(n):
            for x in range(n):
                if mat[y][x] > 0 and not visit[y][x]:  # 일반 블록일 경우에만
                    visit[y][x] = 1
                    group = findGroup(y, x, mat[y][x])

                    if group[0] >= 2:
                        groups.append(group)

        groups = sorted(groups, reverse=True)

        # 블록 그룹 없을 경우엔 종료
        if not groups:
            break

        # 그룹 블록
        score += removeGroup(groups[0])

        # 중력 작용
        gravity()

        # 회전
        rotate()

        # 중력 작용
        gravity()

    return score


if __name__ == "__main__":
    global n, m, mat

    n, m = map(int, f().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, f().split())))

    print(autoPlay())
