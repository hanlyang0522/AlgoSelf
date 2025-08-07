import sys
from collections import deque

queue = deque()

def push(num):
    queue.append(num)

def pop():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)



N = int(sys.stdin.readline())

for n in range(N):
    input = list(sys.stdin.readline().split())

    if input[0] == 'push':
        push(input[1])
    elif input[0] == 'pop':
        pop()
    elif input[0] == 'size':
        size()
    elif input[0] == 'empty':
        empty()
    elif input[0] == 'front':
        front()
    elif input[0] == 'back':
        back()