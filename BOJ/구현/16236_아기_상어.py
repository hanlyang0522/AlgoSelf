import sys

f = sys.stdin.readline

N = int(f())

mat = [[] for _ in range(N)]

for i in range(N):
    mat[i] = list(map(int, f().split()))
    if 9 in mat[i]:
        y, x = i, mat[i].index(9)

shark, cnt = 2, 0


print(cnt)
