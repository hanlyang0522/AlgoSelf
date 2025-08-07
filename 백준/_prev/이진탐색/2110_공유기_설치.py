# 목표: 가장 가까운 공유기의 최대 거리 --> 찾는 것을 거리로 둬야
# 최소: 1, 최대: 처음~마지막 집 사이 거리
# mid가 가능한지 불가능한지 판정

# 이분 탐색이 '원하는 값 k를 찾는 과정' 이라면
# Lower Bound는 '원하는 값 k 이상이 처음 나오는 위치를 찾는 과정' 이며,
# Upper Bound는 '원하는 값 k를 초과한 값이 처음 나오는 위치를 찾는 과정'
# https://blog.naver.com/bestmaker0290/220820005454


import sys

f = sys.stdin.readline


def maxlen(N, C, router):
    l, r = 1, router[-1] - router[0]
    ans = 0

    while l <= r:
        m = (l + r) // 2

        # 설정한 공유기 최소거리로 조건을 만족하는지 탐색
        cnt = 1
        r_prev = router[0]
        for i in range(1, len(router)):
            if router[i] - r_prev >= m:
                cnt += 1
                r_prev = router[i]

        # 제한개수보다 적게 사용했을 경우 --> 간격 감소
        if cnt < C:
            r = m - 1
        # 제한개수보다 같거나 많이 사용했을 경우 --> 거리 증가(같을때도 거리 늘려봄)
        else:
            ans = max(m, ans)
            l = m + 1

    return ans


if __name__ == "__main__":
    N, C = map(int, f().split())
    router = []
    for i in range(N):
        router.append(int(f()))

    print(maxlen(N, C, sorted(router)))
