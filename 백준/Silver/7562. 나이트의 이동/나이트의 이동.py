import sys
from collections import deque

f = sys.stdin.readline

dlist = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]


def bfs(size, start, end):
    visit = [[0 for _ in range(size)] for __ in range(size)]
    dq = deque()
    dq.append((start, 0))

    while dq:
        (y, x), cnt = dq.popleft()
        if visit[y][x] == 1:
            continue
        visit[y][x] = 1

        if y == end[0] and x == end[1]:
            return cnt

        for dy, dx in dlist:
            ty, tx = y + dy, x + dx

            if 0 <= ty <= size - 1 and 0 <= tx <= size - 1:
                dq.append(((ty, tx), cnt + 1))

    return -1


if __name__ == "__main__":
    n = int(f())
    for _ in range(n):
        size = int(f())
        sy, sx = map(int, f().split())
        ey, ex = map(int, f().split())
        print(bfs(size, (sy, sx), (ey, ex)))
