# i -> i+1 가는 최소값 = 1~i 중 최소인 주유소의 기름값 * i~i+1 거리

from os import stat
import sys

f = sys.stdin.readline


def calcMin(n, dist, station):
    ans = 0
    min_cost = station[0]

    for i in range(len(dist)):
        min_cost = min(station[i], min_cost)
        ans += min_cost * dist[i]

    print(ans)


if __name__ == "__main__":
    n = int(f())
    dist = list(map(int, f().split()))
    station = list(map(int, f().split()))

    calcMin(n, dist, station)
