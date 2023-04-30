"""
이분탐색
k <= n <= 10^5
k개의 그룹의 각 sum의 최소값이 최대가 되도록 --> parametric search
해의 범위: 0 ~ sum(x)
"""

import sys


f = sys.stdin.readline


def solve(n):
    """
    n: 각 그룹에서 받을 수 있는 최소값
    점수를 차례로 더해가며 n보다 커질 경우엔 그룹+1
    총 그룹이 k 초과면 false, 이하면 true
    """
    global tests, k

    cnt = 1
    total = 0
    for test in tests:
        total += test

        if total > n:
            cnt += 1
            total = 0

        if cnt > k:
            return False

    return True


if __name__ == "__main__":
    global tests, k

    n, k = map(int, f().split())
    tests = list(map(int, f().split()))

    l, r = 1, sum(tests)
    while l < r:
        mid = (l + r) // 2

        if solve(mid):
            r = mid
        else:
            l = mid + 1

    print(l)
