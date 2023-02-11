"""
누적합 mat 만들어서 좌표기준 계산
"""

import sys

f = sys.stdin.readline


n,m = map(int, f().split())
mat = [[0 for _ in range(n+1)]]
for _ in range(n):
    mat.append([0] + list(map(int, f().split())))


for y in range(1,n+1):
    for x in range(1, n+1):
        mat[y][x]  += mat[y][x-1]

for x in range(1,n+1):
    for y in range(1, n+1):
        mat[y][x] += mat[y-1][x]

for _ in range(m):
    y1,x1,y2,x2 = map(int, f().split())
    ans = mat[y2][x2] - mat[y2][x1-1]-mat[y1-1][x2]+mat[y1-1][x1-1]
    print(ans)