# 1. heapq로 최소값 2개 뽑아서 더하기? --> X
# 2. 매번 정렬해서 2개씩 짝지어 더하기? --> X
# 3. 1번에서 heapify를 안 했기 때문에 fail!

import sys
import heapq

f = sys.stdin.readline


def minCost(k, pglist):
    cnt = 0
    heapq.heapify(pglist)
    while len(pglist) > 1:
        a = heapq.heappop(pglist)
        b = heapq.heappop(pglist)
        cnt += a + b
        heapq.heappush(pglist, a + b)
    print(cnt)


if __name__ == "__main__":
    T = int(f())
    for _ in range(T):
        K = int(f())
        pglist = list(map(int, f().split()))
        minCost(K, pglist)
