from collections import deque

T = int(input())

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(this_loop_index):
    global N, ans_num, ans_move, mat

    y, x = this_loop_index // N, this_loop_index % N

    q = deque()
    q.append((y, x, 1))

    while q:
        cy, cx, cmove = q.popleft()
        cnum = mat[cy][cx]

        if cmove > ans_move:
            ans_move = cmove
            ans_num = mat[y][x]
        elif cmove == ans_move and mat[y][x] < ans_num:
            ans_num = mat[y][x]

        for dy, dx in dirs:
            ty, tx = cy + dy, cx + dx

            if ty < 0 or ty >= N or tx < 0 or tx >= N:
                continue

            if mat[ty][tx] == cnum + 1:
                q.append((ty, tx, cmove + 1))


for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    ans_num = -1
    ans_move = -1

    for i in range(N ** 2):
        bfs(i)

    print(f"#{tc} {ans_num} {ans_move}")
