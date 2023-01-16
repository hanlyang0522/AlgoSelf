from math import ceil
from collections import deque


def solution(progresses, speeds):
    li = deque()

    for prg, spd in zip(progresses, speeds):
        day = ceil((100 - prg) / spd)
        li.append(day)

    ans = []
    idx = li[0]
    num = 0
    while li:
        if li[0] <= idx:
            num += 1
            li.popleft()
        else:
            ans.append(num)
            num = 0
            idx = li[0]
    ans.append(num)

    return ans