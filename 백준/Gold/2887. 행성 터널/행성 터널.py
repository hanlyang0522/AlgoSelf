# 1. 모든 node를 연결시키는 최소 터널 --> min spanning tree --> kruskal
# 2. 모든 행성간 거리: 1e5*1e5 = 1e10

# 3. 행성간 거리를 정렬해서 최소 간격으로 삼음

import sys


f = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def makeTunnel(N, planets):
    dists = []
    for i in range(3):
        planets.sort(key=lambda x: x[i])
        for j in range(1, N):
            dists.append(
                [planets[j - 1][3], planets[j][3], abs(planets[j - 1][i] - planets[j][i])]
            )  # idx1, idx2, dist

    global parents
    parents = [i for i in range(N)]
    total_cost = 0
    dists = sorted(dists, key=lambda x: x[2])

    for i, j, dist in dists:
        if find(i) != find(j):
            total_cost += dist
            union(i, j)

    print(total_cost)


if __name__ == "__main__":
    N = int(f())
    planets = []
    for i in range(N):
        x, y, z = map(int, f().split())
        planets.append([x, y, z, i])  # 행성 idx도 추가

    makeTunnel(N, planets)
