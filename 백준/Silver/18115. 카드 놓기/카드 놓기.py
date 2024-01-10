"""
기초 입출력
"""

import sys
from collections import deque

f = sys.stdin.readline


def solve(n):
    dq = deque()
    skills = list(map(int, f().split()))

    for i in range(1, n + 1):
        if skills[n - i] == 1:
            dq.appendleft(i)
        elif skills[n - i] == 2:
            dq.insert(1, i)
        else:
            dq.append(i)

    for i in dq:
        print(i, end=" ")


if __name__ == "__main__":
    n = int(f())

    solve(n)
