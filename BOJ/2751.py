import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    li.append(int(sys.stdin.readline()))
    
for i in sorted(li):
    sys.stdout.write(str(i)+'\n')