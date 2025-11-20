T = 10

for test_case in range(1, T + 1):
    N = input()
    mat = []

    for _ in range(100):
        mat.append(list(map(int, input().split())))

    x = mat[-1].index(2)
    y = 99

    while y > 0:
        if x < 100 and x > 0 and mat[y][x - 1] == 1:  # 왼쪽 진행
            while x > 0 and mat[y][x - 1] == 1:
                x -= 1
            y -= 1
            continue

        if x >= 0 and x < 99 and mat[y][x + 1] == 1:  # 오른쪽 진행
            while x < 99 and mat[y][x + 1] == 1:
                x += 1
            y -= 1
            continue

        y -= 1

    print(f"#{test_case} {x}")
