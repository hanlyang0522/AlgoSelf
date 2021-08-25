import sys
from collections import deque

queue = deque()

def push_front(num):
    queue.appendleft(num)

def push_back(num):
    queue.append(num)

def pop_front():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def pop_back():
    if queue:
        print(queue.pop())
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

    if input[0] == 'push_front':
        push_front(input[1])
    elif input[0] == 'push_back':
        push_back(input[1])
    elif input[0] == 'pop_front':
        pop_front()
    elif input[0] == 'pop_back':
        pop_back()
    elif input[0] == 'size':
        size()
    elif input[0] == 'empty':
        empty()
    elif input[0] == 'front':
        front()
    elif input[0] == 'back':
        back()