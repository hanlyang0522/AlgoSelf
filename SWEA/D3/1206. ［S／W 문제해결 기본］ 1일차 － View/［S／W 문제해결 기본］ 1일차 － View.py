T = 10

for test_case in range(1, T + 1):
    BD = int(input())
    li = list(map(int, input().split()))
    TOTAL = 0

    for i in range(2, BD - 2):
        max_h = max(li[i - 2], li[i - 1], li[i + 1], li[i + 2])

        if li[i] > max_h:
            TOTAL += li[i] - max_h

    print(f"#{test_case} {TOTAL}")
