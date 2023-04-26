"""
구현
n,m = 5*10^5 -> n*m으로 불가?
k = 100이라 k^3으로 해결 가능
"""

import sys


f = sys.stdin.readline


if __name__ == "__main__":
    n, m, l, k = map(int, f().split())

    star = []
    for _ in range(k):
        x, y = map(int, f().split())
        star.append((x, y))

    maxCnt = 0
    for m in range(k):
        for n in range(k):
            cnt = 0

            for o in range(k):
                if (
                    star[m][0] <= star[o][0] <= star[m][0] + l
                    and star[n][1] <= star[o][1] <= star[n][1] + l
                ):
                    cnt += 1

            maxCnt = max(maxCnt, cnt)

    print(k - maxCnt)
