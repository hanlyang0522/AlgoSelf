#
#
import sys

f = sys.stdin.readline
from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solBest(n, k, li, s, sx, sy):
    # 바이러스 위치 저장
    vira = []
    for i in range(n):
        for j in range(n):
            if li[i][j] != 0:
                vira.append((li[i][j], 0, i, j))  # 종류, 시간, 위치

    vira = sorted(vira, key=lambda x: x[0])  # 바이러스 작은 순으로 정렬
    q = deque(vira)

    while q:
        virus, cnt, y, x = q.popleft()  # 종류, 현재시간, 위치
        if cnt == s:
            continue

        for dy, dx in dir:
            ty, tx = y + dy, x + dx

            if 0 <= ty < n and 0 <= tx < n:
                if li[ty][tx] == 0:
                    li[ty][tx] = virus
                    q.append((virus, cnt + 1, ty, tx))

    return li[sx - 1][sy - 1]


if __name__ == "__main__":
    n, k = map(int, f().split())
    li = []
    for _ in range(n):
        li.append(list(map(int, f().split())))
    s, x, y = map(int, f().split())

    print(solBest(n, k, li, s, x, y))
