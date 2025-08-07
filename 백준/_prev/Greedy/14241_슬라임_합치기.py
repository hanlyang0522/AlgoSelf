import sys

len_ = int(input())
slime = list(map(int, sys.stdin.readline().split()))
score = 0

while len(slime) > 1:
    slime.sort()
    s1 = slime.pop()
    s2 = slime.pop()
    slime.append(s1+s2)
    score = score + s1*s2

print(score)
