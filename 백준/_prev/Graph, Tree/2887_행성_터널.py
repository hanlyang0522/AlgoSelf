# 1. 모든 node를 연결시키는 최소 터널 --> min spanning tree --> kruskal
# 2. 모든 행성간 거리: 1e5*1e5 = 1e10

import sys


f = sys.stdin.readline


def getParent(a):
    if parents[a] == a:
        return a
    else:
        return getParent(parents[a])


def checkUnion(a, b):
    if getParent(a) == getParent(b):
        return True
    else:
        return False


def makeUnion(a, b):
    pa, pb = getParent(a), getParent(b)
    if pa > pb:
        parents[a] = pb
    else:
        parents[b] = pa


def makeTunnel(N, planets):
    planets_dist = []
    for i in range(N):
        for j in range(i + 1, N):
            ax, ay, az = planets[i]
            bx, by, bz = planets[j]
            tmp_dist = min(abs(ax - bx), abs(ay - by), abs(az - bz))

            planets_dist.append([i, j, tmp_dist])

    planets_dist = sorted(planets_dist, key=lambda x: x[2])
    print(planets_dist)

    global parents
    parents = [i for i in range(N)]

    total_cost = 0
    for i, j, dist in planets_dist:
        if not checkUnion(i, j):
            # print(i, j, dist)
            total_cost += dist
            makeUnion(i, j)

    print(total_cost)


if __name__ == "__main__":
    N = int(f())
    planets = []
    for _ in range(N):
        planets.append(list(map(int, f().split())))

    makeTunnel(N, planets)
