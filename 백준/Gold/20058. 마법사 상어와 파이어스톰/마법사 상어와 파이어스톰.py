import sys
from collections import deque

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def move(i):
    global mat
    matNew = [[0 for _ in range(2**n)] for __ in range(2**n)]

    SML = 2**i
    for y in range(0, 2**n, SML):
        for x in range(0, 2**n, SML):
            for ty in range(SML):
                for tx in range(SML):
                    matNew[y + tx][x + SML - 1 - ty] = mat[y + ty][x + tx]
    mat = matNew


def melt():
    global mat
    matNew = [[0 for _ in range(2**n)] for __ in range(2**n)]
    for y in range(BML):
        for x in range(BML):
            cnt = 0
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < BML and 0 <= nx < BML and mat[ny][nx] > 0:
                    cnt += 1
            if cnt < 3:
                matNew[y][x] = max(0, mat[y][x] - 1)
            else:
                matNew[y][x] = mat[y][x]
    mat = matNew


def bfs():
    visit = [[0 for i in range(2**n)] for j in range(2**n)]
    maxBlock = 0

    for y in range(BML):
        for x in range(BML):
            if not visit[y][x] and mat[y][x]:
                visit[y][x] = 1
                block = 1

                q = deque()
                q.append([y, x])
                while q:
                    ty, tx = q.popleft()
                    for dy, dx in dirs:
                        ny, nx = ty + dy, tx + dx
                        if (
                            0 <= ny < BML
                            and 0 <= nx < BML
                            and not visit[ny][nx]
                            and mat[ny][nx]
                        ):
                            visit[ny][nx] = 1
                            q.append([ny, nx])
                            block += 1
                maxBlock = max(maxBlock, block)

    return maxBlock


if __name__ == "__main__":
    f = sys.stdin.readline

    n, q = map(int, f().split())
    BML = 2**n

    mat = []
    for _ in range(BML):
        mat.append(list(map(int, f().split())))
    lli = list(map(int, f().split()))
    for i in range(q):
        if lli[i] > 0:
            move(lli[i])
        melt()

    ice = 0
    for y in range(BML):
        ice += sum(mat[y])
    print(ice)
    print(bfs())
