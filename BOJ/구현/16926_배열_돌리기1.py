import sys

f = sys.stdin.readline

N, M, R = map(int, f().split())

mat = [list(map(int, f().split())) for j in range(N)]
nmat = [[0 for i in range(M)] for j in range(N)]

dir = [[0, -1], [1, 0], [0, 1], [-1, 0]] # LDRU

print(mat)
print(nmat)

for y in range(N):
    for x in range(M):
        
