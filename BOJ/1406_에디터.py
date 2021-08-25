import sys

stack_l = list(sys.stdin.readline().strip())
stack_r = []
n = int(input())

for _ in range(n):
    tmp = sys.stdin.readline()

    if tmp[0] == 'L':
        if stack_l:
            stack_r.append(stack_l.pop())
    
    elif tmp[0] == 'D':
        if stack_r:
            stack_l.append(stack_r.pop())

    elif tmp[0] == 'B':
        if stack_l:
            stack_l.pop()

    elif tmp[0] == 'P':
        stack_l.append(tmp[2])

stack_r.reverse()
stack_l.extend(stack_r)

print(''.join(stack_l))