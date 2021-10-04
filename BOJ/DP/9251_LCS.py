# 1. 답이 엄청 커서 완전 탐색이 안되는가?
# 2. 문제를 정의한 뒤에 부분 문제로 쪼갤 수 있는가? --> 부분수열이??
# 3. 부분 문제가 여러 번 이용 되는가?
# 참고: https://zzonglove.tistory.com/26
import sys

f = sys.stdin.readline

str1 = f()[:-1]
str2 = f()[:-1]
dp = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1  # 가장 마지막 문자가 같으면 str1-1, str2-1의 max 길이+1과 같기 때문
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
