def solution(N, stages):
    di = {}
    num = len(stages)

    for i in range(1, N + 1):
        if num != 0:
            c = stages.count(i)
            di[i] = c / num
            num -= c
        else:
            di[i] = 0

    return sorted(di, key=lambda x: di[x], reverse=True)


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
