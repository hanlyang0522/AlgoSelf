T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    mat = []

    for _ in range(N):
        mat.append(list(map(int, input())))

    SUM = 0
    half = N//2

    for i in range(N):
        if i <= half:
            SUM += sum(mat[i][half-i:half+i+1])
        else:
            SUM += sum(mat[i][i-half:N-(i-half)])

    print(f"#{tc} {SUM}")
