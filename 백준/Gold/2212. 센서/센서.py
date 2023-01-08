"""
1. 최소 범위로 가장 많이 지울 수 있는 순서?? --> X
2. 센서간 간격 재서 작은것부터 고름
"""

import sys

f = sys.stdin.readline


def calcMin(n, k, sensors):
    sensors = sorted(sensors)
    dist = []
    for i in range(len(sensors) - 1):
        dist.append(sensors[i + 1] - sensors[i])
    print(sum(sorted(dist)[:n-k]))


if __name__ == "__main__":
    n = int(f())
    k = int(f())
    sensors = list(map(int, f().split()))
    calcMin(n, k, sensors)
