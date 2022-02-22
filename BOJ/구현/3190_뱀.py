import sys
from collections import deque

f = sys.stdin.readline


def Dummy():
    time = 1
    dir = 1  # 차례대로 U R D L
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    y, x = 0, 0
    snake = deque([[y, x]])
    mat[y][x] = 2

    while True:
        # 머리 진행
        y, x = y + dy[dir], x + dx[dir]

        if y < 0 or y >= N or x < 0 or x >= N:
            return time
        if mat[y][x] == 2:
            return time

        # 사과 아니면 꼬리 제거
        if mat[y][x] != 1:
            temp_y, temp_x = snake.popleft()
            mat[temp_y][temp_x] = 0

        mat[y][x] = 2
        snake.append([y, x])

        if time in dir_ch.keys():
            if dir_ch[time] == "L":
                dir = (dir - 1) % 4
            else:
                dir = (dir + 1) % 4

        time += 1


if __name__ == "__main__":
    N = int(f())
    mat = [[0] * N for _ in range(N)]

    K = int(f())
    for _ in range(K):
        y, x = map(int, f().split())
        mat[y - 1][x - 1] = 1  # 사과 저장

    L = int(f())
    dir_ch = {}
    for _ in range(L):
        d1, d2 = f().split()
        dir_ch[int(d1)] = d2

    print(Dummy())
