'''
1. n명을 태울 수 있는 최소 시간을 이분탐색
2. 최소 시간-1까지 모두 태움 처리
3. 최소시간 기준으로 차례로 1명씩 태우며 n에 도달하면 print
'''


import sys

f = sys.stdin.readline


def isPossible(totoalTime):
    cnt = 0
    for ri in rides:
        cnt += (totoalTime - 1) // ri + 1

    return cnt >= n


if __name__ == "__main__":
    global n
    global rides

    n, m = map(int, f().split())
    rides = list(map(int, f().split()))

    left, right = 0, 2000000000 * 10000 * 30
    while left < right:
        mid = (left + right) // 2

        if isPossible(mid):
            right = mid
        else:
            left = mid + 1

    _left = left - 1
    _n = n
    for ri in rides:
        _n -= (_left - 1) // ri + 1

    for num, ri in enumerate(rides):
        if (left - 1) % ri == 0:
            _n -= 1
        if _n == 0:
            print(num + 1)
            exit()
