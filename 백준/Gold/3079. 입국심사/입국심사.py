# 1. 왜 이분탐색? --> n,m,tk 가 매우 큼!
# 2. 어떻게 이분탐색? --> 걸리는 시간 기준!
# 3. l, r = 최소/최대 시간, max = max(tk)*학생 수
# 4. 좌우 체크는 주어진 시간 내에 검사한 학생수 == m일 경우

import sys

f = sys.stdin.readline


def calcTotal(val, tk):
    cnt = 0
    for t in tk:
        cnt += val // t
    return cnt


def binSearch(n, m, tk):
    l, r = 1, max(tk) * m  # 걸리는 시간 min, max
    ans = r

    mid = (l + r) // 2
    while l <= r:
        mid = (l + r) // 2
        tmp = calcTotal(mid, tk)

        if tmp < m:
            l = mid+1
        else:
            r = mid-1
            ans = min(ans, mid)

    return ans


if __name__ == "__main__":
    n, m = map(int, f().split())
    tk = []
    for _ in range(n):
        tk.append(int(f()))

    print(binSearch(n, m, tk))
