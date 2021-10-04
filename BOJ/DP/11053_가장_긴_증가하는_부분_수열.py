# 1. 답이 엄청 커서 완전 탐색이 안되는가?
# 2. 문제를 정의한 뒤에 부분 문제로 쪼갤 수 있는가?
# 3. 부분 문제가 여러 번 이용 되는가?

import sys

f = sys.stdin.readline

N = int(f())
A_list = list(map(int, f().split()))

dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, N):

    local_max = 0
    for j in range(0, i):
        if A_list[i] > A_list[j]:
            local_max = max(local_max, dp[j])

        dp[i] = local_max + 1  # 현재 idx보다 작은 값들 중 최대배열길이 + 1

print(max(dp))
