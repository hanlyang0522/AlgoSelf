import sys

f = sys.stdin.readline


n, h = map(int, f().split())
suk, jong = [0 for _ in range(h + 1)], [0 for _ in range(h + 1)]

for i in range(n):
    tmp = int(f())
    if i % 2 == 0:
        suk[tmp] += 1
    else:
        jong[tmp] += 1

# 누적합
for i in range(h - 1, -1, -1):
    suk[i] += suk[i + 1]
    jong[i] += jong[i + 1]

# 구간별 최소
mCnt = n
mRng = 0
for i in range(1,h+1): 
    if mCnt > (suk[i]+jong[h-i+1]):
        mCnt = suk[i]+jong[h-i+1]
        mRng = 1
    elif mCnt == suk[i]+jong[h-i+1]:
        mRng += 1

print(mCnt, mRng)