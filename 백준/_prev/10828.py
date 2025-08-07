import sys
from collections import deque

stack = deque()

N = int(sys.stdin.readline())

for n in range(N):
    input = list(sys.stdin.readline().split())

    if input[0] == 'push':
        stack.append(input[1])
    elif input[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif input[0] == 'size':
        print(len(stack))
    elif input[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif input[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])