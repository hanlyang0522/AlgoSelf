import sys

li = [0 for _ in range(10001)]

n = int(sys.stdin.readline())

for i in range(n):
    input = int(sys.stdin.readline())
    li[input] = li[input] + 1

for i in range(1, 10001):
    for j in range(li[i]):
        sys.stdout.write(str(i)+'\n')