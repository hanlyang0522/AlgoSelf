"""
기초 입출력
"""

import sys
from collections import deque

f = sys.stdin.readline


def solve(n):
    dq = deque()
    skills = list(map(int, f().split()))
    skills.reverse()

    for i in range(n):
        if skills[i] == 1:
            dq.appendleft(i + 1)
        elif skills[i] == 2:
            dq.insert(1, i + 1)
        else:
            dq.append(i + 1)

    for i in dq:
        print(i, end=" ")


if __name__ == "__main__":
    n = int(f())

    solve(n)
