import sys
f = sys.stdin.readline

N, M = map(int, f().split())
y_list = []
x_list = []

for i in range(M):
    y, x = map(int, f().split())
    y_list.append(y)
    x_list.append(x)

# 평균이 아니라 중간값을 사용해야함
y_list.sort()
x_list.sort()
y_mean = y_list[M//2]
x_mean = x_list[M//2]

dist = 0
for y, x in zip(y_list, x_list):
    dist += abs(y-y_mean) + abs(x-x_mean)

print(dist)
