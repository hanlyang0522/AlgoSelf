import sys

f = sys.stdin.readline

pos, neg = [], []
ans = 0

n = int(f())
for _ in range(n):
    num = int(f())
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)

pos = sorted(pos)
neg = sorted(neg, reverse=True)
# print(pos, neg)

while len(pos) > 1:
    a, b = pos.pop(), pos.pop()
    if b != 1:
        ans += a * b
    else:
        ans += a + b
if len(pos) > 0:
    ans += pos[0]

while len(neg) > 1:
    a, b = neg.pop(), neg.pop()
    ans += a * b
if len(neg) > 0:
    ans += neg[0]

print(ans)
