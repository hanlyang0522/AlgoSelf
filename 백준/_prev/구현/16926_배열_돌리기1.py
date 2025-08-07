import sys
from collections import deque

f = sys.stdin.readline

N, M, R = map(int, f().split())

mat = [list(map(int, f().split())) for j in range(N)]


def rotate(y, x, height, width):
    global mat
    q = deque()

    # (y,x)부터 시계방향으로 저장
    for i in range(x, x + width):
        q.append(mat[y][i])

    for i in range(y + 1, y + height):
        q.append(mat[i][x + width - 1])

    for i in range(x + width - 2, x, -1):
        q.append(mat[y + height - 1][i])

    for i in range(y + height - 1, y, -1):
        q.append(mat[i][x])

    # 반시계 회전
    q.rotate(-R)

    # (y,x)부터 시계방향으로 저장
    for i in range(x, x + width):
        mat[y][i] = q.popleft()

    for i in range(y + 1, y + height):
        mat[i][x + width - 1] = q.popleft()

    for i in range(x + width - 2, x, -1):
        mat[y + height - 1][i] = q.popleft()

    for i in range(y + height - 1, y, -1):
        mat[i][x] = q.popleft()


y, x, height, width = 0, 0, N, M

while height != 0 and width != 0:
    rotate(y, x, height, width)
    y += 1
    x += 1
    height -= 2
    width -= 2

for i in range(N):
    for j in range(M):
        print(mat[i][j], end=" ")
    print()
