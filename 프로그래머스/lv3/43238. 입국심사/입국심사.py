"""
n = 10^9라 최소 O(NlogN)으로 풀어야함
"""


def isPossible(target):
    cnt = n
    for ti in times:
        cnt -= target // ti

    return cnt <= 0


def solution(_n, _times):
    global n
    global times
    n = _n
    times = _times

    left, right = 0, 1000000000 * 1000000000

    while left < right:
        mid = (left + right) // 2

        if isPossible(mid):
            right = mid
        else:
            left = mid + 1

    return left