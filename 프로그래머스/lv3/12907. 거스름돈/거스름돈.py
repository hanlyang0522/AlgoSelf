def solution(n, money):
    dp = [[0] * (n + 1) for _ in range(len(money) + 1)]

    for y in range(1, len(money) + 1):
        dp[y][0] = 1  # 아무것도 안 고르는 것도 한 가지 경우의 수로 취급

        for x in range(1, n + 1):
            dp[y][x] = dp[y - 1][x]  # 이전 loop 경우의 수 복사

            if x >= money[y - 1]:  # (현재 금액 - 현재 동전)의 경우의 수 추가
                dp[y][x] += dp[y][x - money[y - 1]]
                dp[y][x] %= 100000000007

    return dp[len(money)][n]