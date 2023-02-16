"""
빡구현
"""

import sys
from collections import deque

f = sys.stdin.readline

dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


if __name__ == "__main__":
    n, m, k = map(int, f().split())
    farm = [[5 for _ in range(n)] for __ in range(n)]

    a = []
    for _ in range(n):
        a.append(list(map(int, f().split())))

    # 매 좌표마다 dq를 이용해 나이순 정렬 과정을 없앰
    tree = [[deque() for _ in range(n)] for __ in range(n)]
    for _ in range(m):
        x, y, z = map(int, f().split())
        tree[x - 1][y - 1].append(z)

    for _ in range(k):
        # S/S
        for x in range(n):
            for y in range(n):
                alive, dead = deque(), 0
                for z in tree[x][y]:
                    # 양분 먹거나
                    if farm[x][y] >= z:
                        farm[x][y] -= z
                        alive.append(z + 1)
                    # 죽거나
                    else:
                        dead += z // 2
                tree[x][y] = alive
                # 죽은 나무 양분에 추가
                farm[x][y] += dead

        # F/W
        # autumn()
        tmpTrees = []
        for x in range(n):
            for y in range(n):
                # 번식
                for k in range(len(tree[x][y])):
                    if tree[x][y][k] % 5 == 0:
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].appendleft(1)
                # 양분 추가
                farm[x][y] += a[x][y]

    total = 0
    for x in range(n):
        for y in range(n):
            total += len(tree[x][y])
    print(total)
