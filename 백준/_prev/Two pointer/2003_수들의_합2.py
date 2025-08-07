import sys

f = sys.stdin.readline

N, M = map(int, f().split())
numli = list(map(int, f().split()))

cnt = 0
j = 0
i_sum = 0

for i in range(N):
    while i_sum < M and j < N:
        i_sum += numli[j]
        j += 1
    if i_sum == M:
        cnt += 1
    i_sum -= numli[i]

print(cnt)
