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
                vira.append((li[i][j], 1, i, j))  # 종류, 시간, 위치

    vira = sorted(vira, key=lambda x: x[0])  # 바이러스 작은 순으로 정렬
    q = deque(vira)

    while q:
        virus, cnt, x, y = q.popleft()  # 종류, 현재시간, 위치
        if cnt == s:
            continue

        for dy, dx in dir:
            ty, tx = y + dy, x + dx

            if 0 <= ty < n and 0 <= tx < n:
                if li[ty][tx] == 0:
                    li[ty][tx] = virus
                    q.append((virus, cnt + 1, ty, tx))

    print(li)
    return li[sx - 1][sy - 1]


def Solution(n, k, li, s, sx, sy):
    k_li = [[] for _ in range(k + 1)]

    # 바이러스별 위치 저장
    for i in range(n):
        for j in range(n):
            if li[i][j] != 0:
                k_li[li[i][j]].append((i, j))

    # print(k_li)

    # 매 초마다
    while s:
        # 바이러스마다 퍼져나감
        for k_tmp in range(1, k + 1):
            q = deque(k_li[k_tmp])
            tmp_li = []
            # print(q)

            while q:
                y, x = q.pop()

                for dy, dx in dir:
                    ty, tx = y + dy, x + dx

                    if 0 <= ty < n and 0 <= tx < n:
                        if li[ty][tx] == 0:
                            li[ty][tx] = k_tmp
                            tmp_li.append((ty, tx))
            k_li[k_tmp] = tmp_li

        # 초 역순으로 계산
        s -= 1

    return li[sx - 1][sy - 1]


if __name__ == "__main__":
    n, k = map(int, f().split())
    li = []
    for _ in range(n):
        li.append(list(map(int, f().split())))
    s, x, y = map(int, f().split())

    print(Solution(n, k, li, s, x, y))
    print(solBest(n, k, li, s, x, y))
