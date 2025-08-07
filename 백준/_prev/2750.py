import sys

N = int(sys.stdin.readline())

li = []

for _ in range(N):
    li.append(int(sys.stdin.readline()))

li.sort()

for _ in range(N):
    print(li[_])