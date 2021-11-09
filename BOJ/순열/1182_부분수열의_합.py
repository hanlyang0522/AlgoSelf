import sys
from itertools import combinations

f = sys.stdin.readline

N, S = map(int, f().split())
li = list(map(int, f().split()))

cnt = 0

for i in range(1, N + 1):
    for c in combinations(li, i):
        if sum(c) == S:
            cnt += 1

print(cnt)
