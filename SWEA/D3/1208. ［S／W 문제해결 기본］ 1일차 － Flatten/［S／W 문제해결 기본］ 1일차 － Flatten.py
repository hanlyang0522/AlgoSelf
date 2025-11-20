T = 10

for test_case in range(1, T + 1):
    DUMP = int(input())
    box = list(map(int, input().split()))
    # box = sorted(box, reverse=True)

    for i in range(DUMP):
        maxi = box.index(max(box))
        mini = box.index(min(box))

        box[maxi] -= 1
        box[mini] += 1

        if max(box) - min(box) <= 1:
            break

    print(f"#{test_case} {max(box) - min(box)}")
