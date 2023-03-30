import sys

sys.setrecursionlimit(int(1e9))


def recursion(n):
    global memo

    if memo[n] == -1:
        memo[n] = recursion(n - 1) + recursion(n - 2)

    return memo[n] % 1000000007


def solution(n):
    global memo
    memo = [-1] * (n + 3)

    memo[0] = memo[1] = 1

    return recursion(n)