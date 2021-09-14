# 특성값이 0에 가깝게 만드는게 목표
# combination 사용하니 메모리 초과
# lo, hi, goal은 어떻게 설정??
# lo, hi를 양끝단으로 잡고 최대 N번 탐색 --> 투포인터 알고리즘!!

import sys
f = sys.stdin.readline

N = int(f())
sol = sorted(list(map(int, f().split())))

minv = sys.maxsize
lo, hi = 0, N-1
ans1, ans2 = 0, N-1 # 정답 idx
while lo < hi:
    tmp = sol[lo] + sol[hi]

    if abs(tmp) < minv:
        minv = abs(tmp)
        ans1, ans2 = lo, hi

    if tmp < 0: # 합이 0보다 작으므로 지금보다 커져야 0에 가까워질것        
        lo += 1
    else:       # 합이 0보다 크므로 지금보다 작아져야 0에 가까워질것
        hi -= 1

print(sol[ans1], sol[ans2])