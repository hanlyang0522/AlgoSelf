def solution(n):
    li = [[0 for i in range(j + 1)] for j in range(n)]
    y, x = -1, 0
    num = 0

    for i in range(n):  # 0~5
        for j in range(i, n):  # 6~1
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            else:
                y -= 1
                x -= 1

            num += 1
            li[y][x] = num

    print(sum(li, []))


def solution2(n):
    li = [[0 for i in range(j + 1)] for j in range(n)]
    d, x, y = 0, 0, -1
    num = 1

    while n:  # 방향 별 길이
        cnt = 0
        while cnt < n:
            if d % 3 == 0:
                y += 1
            elif d % 3 == 1:
                x += 1
            else:
                y -= 1
                x -= 1

            cnt += 1
            li[y][x] = num
            num += 1

        n -= 1
        d += 1

    print(sum(li, []))


solution(3)
solution2(3)
solution(4)
solution2(4)
solution(5)
solution2(5)
