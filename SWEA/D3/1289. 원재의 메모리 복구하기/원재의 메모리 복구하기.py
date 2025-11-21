T = int(input())

for tc in range(1, T + 1):
    li = '0' + str(input())

    total = 0

    for i in range(1, len(li)):
        if li[i - 1] != li[i]:
            total += 1

    print(f"#{tc} {total}")
