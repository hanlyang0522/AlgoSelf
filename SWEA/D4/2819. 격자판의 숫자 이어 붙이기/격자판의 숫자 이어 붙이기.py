T = int(input())

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(y, x, num_curr: str):
    global num
    global mat

    if len(num_curr) == 7:
        num.add(num_curr)
        return 

    for dy, dx in dirs:
        yy, xx = y + dy, x + dx

        if yy < 0 or yy > 3 or xx < 0 or xx > 3:
            continue

        dfs(yy, xx, num_curr + mat[yy][xx])


for tc in range(1, T + 1):
    N = 4

    mat = []

    for _ in range(N):
        mat.append((list(map(str, input().split()))))

    num = set()

    for i in range(N):
        for j in range(N):
            dfs(i, j, mat[i][j])

    print(f"#{tc} {len(num)}")
