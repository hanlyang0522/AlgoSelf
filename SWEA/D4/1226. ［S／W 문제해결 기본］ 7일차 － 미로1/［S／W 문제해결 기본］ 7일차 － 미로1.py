from collections import deque

T = 10

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for tc in range(1, T + 1):
    N = 16
    _ = input()

    visit = set()
    mat = []

    for _ in range(N):
        mat.append(list(input()))

    q = deque()
    q.append((1, 1))
    visit.add((1, 1))
    flag = False

    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            yy, xx = y + dy, x + dx

            # 벽
            if yy == 0 or yy == N - 1 or xx == 0 or xx == N - 1:
                continue

            if mat[yy][xx] == '1':
                continue

            # 이미 방문
            if (yy, xx) in visit:
                continue

            # 도착
            if mat[yy][xx] == '3':
                print(f"#{tc} {1}")
                flag = True

            # 방문문
            q.append((yy, xx))
            visit.add((yy, xx))
    
    if not flag:
        print(f"#{tc} {0}")
