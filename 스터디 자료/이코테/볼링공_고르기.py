# 1. 서로 다른 무게
# 2. 볼링공N 최대무게M --> 무게당 개수로 정리!

import sys
from itertools import combinations

f = sys.stdin.readline


def ball_cnt(N, M, balls):
    # for b1, b2 in combinations(balls, 2):
    #     if b1 != b2:
    #         cnt += 1

    li = [0] * 11

    for b in balls:
        li[b] += 1

    cnt = 0
    for i in range(1, M):
        cnt += li[i] * sum(li[i + 1 :])
    print(cnt)


if __name__ == "__main__":
    # N, M = 5, 3
    # balls = 1, 3, 2, 3, 2
    # ball_cnt(N, M, balls)

    # N, M = 8, 5
    # balls = 1, 5, 4, 3, 2, 4, 5, 2
    # ball_cnt(N, M, balls)

    N, M = map(int, f().split())
    balls = list(map(int, f().split()))
