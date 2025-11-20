T = 10

for test_case in range(1, T + 1):
    N = input()

    rowM, colM, diagM, diagM2 = 0, 0, 0, 0

    col = [0] * 100

    for i in range(100):
        li = list(map(int, input().split()))

        rowM = max(rowM, sum(li))
        diagM += li[i]
        diagM2 += li[-1 - i]

        for j in range(100):
            col[j] += li[j]

    colM = max(col)
    totalMax = max(rowM, colM, diagM, diagM2)

    print(f"#{test_case} {totalMax}")
