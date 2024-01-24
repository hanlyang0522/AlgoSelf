"""
1. popleft 해서 
"""

import sys
from collections import deque

f = sys.stdin.readline


def solve(n, w, L, trucks):
    time = 0
    bridge = deque([0] * w)
    idx = 0

    while idx < n:
        time += 1
        bridge.popleft()

        if sum(bridge) + trucks[idx] <= L:
            bridge.append(trucks[idx])
            idx += 1
        else:
            bridge.append(0)

    while bridge:
        time += 1
        bridge.popleft()
        
    print(time)


if __name__ == "__main__":
    n, w, L = map(int, f().split())
    trucks = list(map(int, f().split()))

    solve(n, w, L, trucks)
