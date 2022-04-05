#
#
import sys
import bisect
from collections import deque

f = sys.stdin.readline


def minComp(n, clist):
    dq = deque(clist)
    sum = 0
    while len(dq) > 1:
        a = dq.popleft()
        b = dq.popleft()
        sum += a + b
        bisect.insort(dq, a + b)

    return sum


if __name__ == "__main__":
    n = int(f())
    clist = []
    for _ in range(n):
        clist.append(int(f()))
    clist.sort()

    print(minComp(n, clist))
