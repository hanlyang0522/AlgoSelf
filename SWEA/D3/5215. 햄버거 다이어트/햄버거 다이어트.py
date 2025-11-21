T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())

    food = []  # 맛, 칼로리

    for _ in range(N):
        food.append(list(map(int, input().split())))

    food = sorted(food, key=lambda x: x[1])

    mat = [[0] * (L + 1) for _ in range(N + 1)]

    for y in range(1, N + 1):  # 재료
        taste, cal = food[y - 1]

        for x in range(1, L + 1):  # 무게
            if x < cal:
                mat[y][x] = mat[y - 1][x]
            else:
                mat[y][x] = max(mat[y - 1][x], mat[y - 1][x - cal] + taste)

    print(f"#{tc} {mat[-1][-1]}")
