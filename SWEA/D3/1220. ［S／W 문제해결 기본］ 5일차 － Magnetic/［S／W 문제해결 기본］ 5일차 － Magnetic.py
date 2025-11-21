T = 10

for tc in range(1, T + 1):
    N = int(input())

    mat = []

    for _ in range(N):
        mat.append(list(map(int, input().split())))

    mat = list(map(list, zip(*mat)))

    total = 0

    for y in range(N):
        is_one = False

        for x in range(N):
            if mat[y][x] == 1:
                is_one = True
            elif mat[y][x] == 2 and is_one:
                total += 1
                is_one = False

    print(f"#{tc} {total}")
