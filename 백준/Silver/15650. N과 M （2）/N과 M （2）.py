"""
백트래킹
"""


import sys
from collections import deque

f = sys.stdin.readline


def backtrack(s, idx):
    global used

    if len(s) >= LENGTH:
        s = sorted(s)
        print(*s)
        return

    for i in range(NUMS):
        if not used[i] and i > idx:
            used[i] = 1
            backtrack(s + [numLi[i]], i)
            used[i] = 0


if __name__ == "__main__":
    global used
    global numLi
    global LENGTH
    global NUMS

    n, m = map(int, f().split())

    used = [0 for _ in range(n)]
    numLi = [i for i in range(1, n + 1)]
    LENGTH = m
    NUMS = n

    backtrack([], -1)
