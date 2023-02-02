"""
2539. 
1. 최소 크기 -> 크기를 m으로 이분탐색
2. 색종이는 무조건 도화지 밑변에 붙여야함!! 문제를 똑바로 읽자!!
"""

import sys

f = sys.stdin.readline

h, w = map(int, f().split())
maxPaper, wrongs = int(f()), int(f())  # num_paper, wrong
xList = []
yMax = 0
for _ in range(wrongs):
    y, x = map(int, f().split())
    yMax = max(yMax, y)
    xList.append(x)
xList.sort()


def checkOk(leng):
    idx = xList[0] + leng - 1
    nPaper = 1
    for x in xList:
        if x <= idx:
            continue
        else:
            idx = x + leng - 1
            nPaper += 1

        if nPaper > maxPaper:
            return False

    return True


start, end = yMax, min(h, w)
ans = end
while start <= end:
    mid = (start + end) // 2

    if checkOk(mid):
        ans = mid
        end = mid - 1
    else:
        start = mid + 1


print(ans)
