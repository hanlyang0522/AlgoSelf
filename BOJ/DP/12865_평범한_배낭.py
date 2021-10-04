# 1. 답이 엄청 커서 완전 탐색이 안되는가?
# 2. 문제를 정의한 뒤에 부분 문제로 쪼갤 수 있는가?
# 3. 부분 문제가 여러 번 이용 되는가?

# i번째 물품을 넣은것 vs 안 넣은것 비교 -> 뭘 뺄건데?
# 물품은 무게순? 가치순?
# --> 매 iter마다 가방의 무게를 기준으로 dp

import sys

f = sys.stdin.readline

N, K = map(int, f().split())
dp = [[0 for i in range(K + 1)] for j in range(N + 1)]

for i in range(1, N + 1):
    W, V = map(int, f().split())

    for j in range(1, K + 1):
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

print(dp[-1][-1])
