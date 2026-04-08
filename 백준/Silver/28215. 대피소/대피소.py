import sys
from itertools import combinations

f = sys.stdin.readline


def solve():
    N, K = map(int, f().split())
    mat = []

    for i in range(N):
        mat.append(list(map(int, f().split())))

    # print(mat)

    nums = [i for i in range(N)]

    combs = combinations(nums, K)
    
    # print(combs)

    total = 1e9

    for co in combs:
        # print(co)

        co_max_dist = 0

        # 거리 계산
        for i in range(N):
            if i in co:
                continue

            y,x = mat[i]

            tmp = 1e9

            # 대피소 별로 최단 거리 찾음
            for c in co:
                cy, cx = mat[c]

                dist = abs(cy-y) + abs(cx-x)

                if dist < tmp:
                    tmp = dist

            co_max_dist = max(co_max_dist, tmp)

        if co_max_dist < total:
            total = co_max_dist

    print(total)



    pass


if __name__ == "__main__":
    solve()