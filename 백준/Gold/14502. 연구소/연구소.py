# 바이러스 퍼지는거 -> bfs로 처리
# 벽 어디 세울지: 64C3 --> 최대 41664 가지
import sys
from itertools import combinations
from collections import deque
import copy

f = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(n, m, li):
    q = deque()
    for i in range(n):
        for j in range(m):
            if li[i][j] == 2:
                q.append([i, j])

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < n and 0 <= nx < m:
                if li[ny][nx] == 0:
                    li[ny][nx] = 2
                    q.append([ny, nx])

    cnt = 0
    for l in li:
        cnt += l.count(0)
    return cnt


def safeSpace(n, m, li):
    walls = list(combinations(range(n * m), 3))
    ans = 0
    # print(walls)

    for wall in walls:
        li2 = copy.deepcopy(li)

        # 벽 설정
        flag = True
        for w in wall:
            y, x = w // m, w % m
            if li2[y][x] != 0:
                flag = False
                break
            li2[y][x] = 1
        if not flag:
            continue

        # print(li2)
        # 바이러스에서 BFS
        ans = max(ans, bfs(n, m, li2))

    return ans


if __name__ == "__main__":
    n, m = map(int, f().split())  # 세로, 가로
    li = []
    for i in range(n):
        li.append(list(map(int, f().split())))

    # print(li)
    print(safeSpace(n, m, li))
