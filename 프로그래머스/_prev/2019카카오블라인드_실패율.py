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

def solution2(N, stages):
    li = [[i + 1, 0] for i in range(N)]  # stage, 실패/도달
    tot = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)
        if tot!=0:
            li[i - 1][1] = cnt / tot
        else:
            li[i-1][1]==0
        tot -= cnt

    li = sorted(li, key=lambda x: x[1], reverse=True)
    return [li[i][0] for i in range(N)]


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
