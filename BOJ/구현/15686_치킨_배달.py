# N, M이 모두 50을 넘지 않기 때문에 완전탐색으로 가능
import sys
from itertools import combinations

f = sys.stdin.readline


def min_chickenroad(home, chicken, M):
    total_dist = sys.maxsize
    for chick in combinations(chicken, M):
        tmp_dist = 0
        for hy, hx in home:
            tmp_dist += min([abs(hy - cy) + abs(hx - cx) for cy, cx in chick])
        total_dist = min(total_dist, tmp_dist)
    print(total_dist)


if __name__ == "__main__":
    N, M = map(int, f().split())
    home = []
    chicken = []
    for i in range(N):
        tmp = list(map(int, f().split()))
        for j in range(N):
            if tmp[j] == 1:
                home.append([i, j])
            elif tmp[j] == 2:
                chicken.append([i, j])

    min_chickenroad(home, chicken, M)
