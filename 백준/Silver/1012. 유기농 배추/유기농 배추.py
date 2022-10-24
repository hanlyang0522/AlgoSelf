import sys
from collections import deque

dir_ = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(baechoo, w, h, n):
    n_cater = 0
    stack = deque()

    for y in range(h):
        for x in range(w):
            # if '1' not in baechoo[y]:
            #     continue

            if baechoo[y][x] == 1:
                stack.append([y, x])
                n_cater = n_cater + 1

                if n_cater == n:
                    return n_cater

                while stack:
                    yy, xx = stack.pop()

                    for dy, dx in dir_:
                        if yy+dy<0 or yy+dy>h-1 or xx+dx<0 or xx+dx>w-1:
                            continue
                        if baechoo[yy+dy][xx+dx] == 1:
                            baechoo[yy+dy][xx+dx] = 0
                            stack.append([yy+dy, xx+dx])

    return n_cater


iter_ = int(sys.stdin.readline())

for _ in range(iter_):
    w, h, n = list(map(int, sys.stdin.readline().split()))
    baechoo = [[0 for i in range(w)] for j in range(h)]

    for i in range(n):
        x, y = list(map(int, sys.stdin.readline().split()))
        baechoo[y][x] = 1

    print(bfs(baechoo, w, h, n))