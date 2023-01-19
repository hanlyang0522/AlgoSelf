"""
1. 가장 마지막부터 방문
"""
from collections import deque


def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    dist = 0
    d, p = 0, 0

    for i in range(n):
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            # 음수만큼 이전 방문에서 처리했다는 뜻
            d -= cap
            p -= cap
            dist += (n - i) * 2

    return dist