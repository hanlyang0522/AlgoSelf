# 문제 유형이 이진탐색 --> 무엇을 이진탐색할 것인가?
# 처음엔 각 lect를 나누는 구간을 탐색? --> 이진탐색X, 탐색방법 불명확
# output은 블루레이 당 강의 길이 --> 블루레이에 담기는 강의 길이가 언제 False/True 바뀌는지
import sys
f = sys.stdin.readline

# 강의는 sorted list
N, M = map(int, f().split())
lect = list(map(int, f().split()))

# 그러면 lo, hi는 블루레이당 강의 길이의 min, MAX
# 블루레이 1개당 강의 1개 들어가도 최소 길이는 max(lect)로 나옴
lo, hi = max(lect)-1, sum(lect)

# lo ~ F, F, F, T, T ~ hi의 범위에서 F->T가 되는 경계를 찾아야됨
def check(mid):
    sum = lect[0]
    cnt = 1

    for i in range(1, len(lect)):
        if sum + lect[i] <= mid:
            sum += lect[i]
        else:
            cnt += 1
            sum = lect[i]
    
    if cnt <= M:
        return True
    else:
        return False

# check가 False -> True로 바뀌는 시점 = hi
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid) != True:
        lo = mid
    else:
        hi = mid

print(hi)