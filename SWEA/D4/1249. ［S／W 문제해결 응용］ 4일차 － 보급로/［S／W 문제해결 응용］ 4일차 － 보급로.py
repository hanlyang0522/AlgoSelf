from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    mat = []

    for _ in range(N):
        mat.append(list(map(int, input())))

    q = deque()
    q.append((0, 0, 0))

    visit = [[-1] * N for _ in range(N)]
    visit[0][0] = 0

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # y,x

    while q:
        y, x, cost = q.popleft()

        for dy, dx in dirs:
            yy = y + dy
            xx = x + dx

            if yy < 0 or yy >= N or xx < 0 or xx >= N:
                continue

            curCost = cost + mat[yy][xx]

            if visit[yy][xx] == -1 or curCost < visit[yy][xx]:
                visit[yy][xx] = curCost
                q.append((yy, xx, curCost))

    ANS = visit[-1][-1]

    print(f"#{test_case} {ANS}")
