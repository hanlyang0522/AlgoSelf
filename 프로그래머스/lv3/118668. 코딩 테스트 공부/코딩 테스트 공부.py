def solution(alp, cop, problems):
    gA = sorted(problems, key=lambda x: x[0])[-1][0]
    gC = sorted(problems, key=lambda x: x[1])[-1][1]
    alp = min(alp, gA)
    cop = min(cop, gC)
    
    dp = [[int(1e9) for _ in range(gC + 1)] for __ in range(gA + 1)]
    dp[alp][cop] = 0

    for y in range(alp, gA + 1):
        for x in range(cop, gC + 1):
            # 학습할 경우와 원래 시간 중 뭐가 최소인지 비교
            if y < gA:
                dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + 1)
            if x < gC:
                dp[y][x + 1] = min(dp[y][x + 1], dp[y][x] + 1)

            for alpReq, copReq, alpRwd, copRwd, time in problems:
                # 문제를 풀 수 있을 경우
                if y >= alpReq and x >= copReq:
                    newAlp = min(y + alpRwd, gA)
                    newCop = min(x + copRwd, gC)
                    newTime = dp[y][x] + time
                    dp[newAlp][newCop] = min(dp[newAlp][newCop], newTime)

    return dp[-1][-1]

