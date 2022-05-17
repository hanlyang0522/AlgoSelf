# 1. 동물 좌표에서 x축 폭 구함
# 2. upper-lower로 폭에 속하는 사대의 val+=1
# 2-1. 그러면 사대 정렬해두기
# 3. 사대의 max값 출력
# --> 사대는 움직일 수 있음!!
# --------------
# 1. 동물 기준으로 가까운 좌, 우 사대 구함
# 2. 좌, 우 사대에서 쏠 수 있다면 cnt += 1
import sys

f = sys.stdin.readline

# li 중 tg 이상인 값 중 최소 idx
def lower_bound(li, tg):
    lo, hi = 0, len(li) - 1

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if li[mid] >= tg:
            hi = mid
        else:
            lo = mid

    return lo


# li 중 tg 초과인 값 중 최소 idx
def upper_bound(li, tg):
    lo, hi = 0, len(li) - 1

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if li[mid] > tg:
            hi = mid
        else:
            lo = mid

    return hi


def shootCount(m, n, l, m_list, n_list):
    m_list = sorted(m_list)
    cnt = 0

    for x, y in n_list:
        if y > l:
            continue

        # 이분탐색으로 x이하(start)/초과(end)가 되는 경계를 찾음
        start, end = 0, len(m_list) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if m_list[mid] <= x:
                start = mid
            else:
                end = mid

        if abs(x - m_list[end]) + y <= l or abs(x - m_list[end - 1]) + y <= l:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    m, n, l = map(int, f().split())
    m_list = list(map(int, f().split()))
    n_list = []
    for _ in range(n):
        n_list.append(list(map(int, f().split())))

    # print("------------------")
    shootCount(m, n, l, m_list, n_list)
