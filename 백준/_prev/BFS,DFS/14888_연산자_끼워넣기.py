# 연산자만 입력하고 값 계산은 마지막에!

import sys
from collections import deque

f = sys.stdin.readline

M = -1e9
m = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global M, m
    if depth == N:
        M = max(total, M)
        m = min(total, m)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


if __name__ == "__main__":
    N = int(f())
    num = list(map(int, f().split()))
    opr = list(map(int, f().split()))
    dfs(1, num[0], *opr)

    print(M, m, end="\n")
