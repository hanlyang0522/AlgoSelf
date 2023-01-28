"""
1. n = 10^5, 2차원배열 만들면 10^10이라 바로 초과
2. 이분탐색으로 풀기: m 보다 작은 수의 갯수를 세기 == m이 몇번째 수인지
3. l, r = 0, n*n
4. m보다 작은 수의 갯수: m//i의 총합(i=1~n), 이때 m//i가 n을 넘을 수 없다
각 행은 자연수의 곱이기 때문문
"""

import sys

f = sys.stdin.readline

n = int(f())
k = int(f())

l, r = 1, k # 중복되는 수가 있어 k번째 수는 k보다 클 수 없음
while l <= r:
    mid = (l + r) // 2

    cnt = 0
    for i in range(1, n + 1):  # 각 행 별로 m보다 작은 수의 갯수
        cnt += min(mid // i, n)  # 각 행의 최대 길이는 n

    # 종료 조건: cnt == k-1일 경우
    if cnt >= k:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
