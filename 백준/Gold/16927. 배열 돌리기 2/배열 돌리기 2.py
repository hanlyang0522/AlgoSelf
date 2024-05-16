import sys
from collections import deque

f = sys.stdin.readline


def solve(r, c, T):
    global mat

    mat = [list(map(int, f().split())) for _ in range(r)]

    y, x = 0, 0
    h, w = r, c

    while h != 0 and w != 0:
        rotate(y, x, h, w, T)

        y += 1
        x += 1
        h -= 2
        w -= 2

    for y in range(r):
        for x in range(c):
            print(mat[y][x], end=" ")
        print()


def rotate(y, x, h, w, T):
    q = deque()

    for i in range(x, x + w):
        q.append(mat[y][i])

    for i in range(y + 1, y + h):
        q.append(mat[i][x + w - 1])

    for i in range(x + w - 2, x, -1):
        q.append(mat[y + h - 1][i])

    for i in range(y + h - 1, y, -1):
        q.append(mat[i][x])

    T = T % (2 * w + 2 * h - 4)
    q.rotate(-T)

    for i in range(x, x + w):
        mat[y][i] = q.popleft()

    for i in range(y + 1, y + h):
        mat[i][x + w - 1] = q.popleft()

    for i in range(x + w - 2, x, -1):
        mat[y + h - 1][i] = q.popleft()

    for i in range(y + h - 1, y, -1):
        mat[i][x] = q.popleft()


if __name__ == "__main__":
    r, c, T = map(int, f().split())

    solve(r, c, T)
