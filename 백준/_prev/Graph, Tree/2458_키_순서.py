# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
# --> 1

# 6 7
# 1 3
# 1 5
# 3 4
# 5 4
# 4 2
# 4 6
# 5 2
# --> 2

# 6 3
# 1 2
# 2 3
# 4 5
# --> 0

# 1. 플로이드로 모든 최단경로 구함
# 2. 자기로 오는 + 자기가 가는 경로 개수 합이 N-1이 되면 cnt += 1
# 3. 아니면
import sys

f = sys.stdin.readline


def hOrder(N, M, compares):
    dp = [[10000 if _ != __ else 0 for _ in range(N)] for __ in range(N)]

    for l, h in compares:
        dp[h - 1][l - 1] = 1

    # print(dp)

    for k in range(N):
        for a in range(N):
            for b in range(N):
                dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

    print(dp)

    cnt = 0

    for i in range(N):
        flag = True
        for j in range(N):
            if i != j:
                if dp[i][j] == 10000 and dp[j][i] == 10000:
                    flag = False
                    break
        if flag:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    N, M = map(int, f().split())
    compares = []
    for _ in range(M):
        compares.append(list(map(int, f().split())))

    hOrder(N, M, compares)
