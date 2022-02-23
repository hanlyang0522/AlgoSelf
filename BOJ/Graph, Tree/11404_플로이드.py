# 모든 도시에서 각 도시로 가는 최소비용 --> 와샬-플로이드

import sys

f = sys.stdin.readline


def floyd(n, m, bus):
    graph = [[sys.maxsize if i != j else 0 for i in range(n)] for j in range(n)]
    for (a, b, c) in bus:
        if c < graph[a - 1][b - 1]:
            graph[a - 1][b - 1] = c
    # print(graph)

    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        if i != n - 1:
            print()


if __name__ == "__main__":
    n = int(f())
    m = int(f())
    bus = []
    for i in range(m):
        bus.append(list(map(int, f().split())))

    floyd(n, m, bus)
