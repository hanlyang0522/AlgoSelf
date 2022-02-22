import sys

f = sys.stdin.readline


def floyd(n, m, bus):
    graph = [[0 for i in range(n)] for j in range(n)]
    for (a, b, c) in bus:
        graph[a - 1][b - 1] = c
    print(graph)

    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return graph


if __name__ == "__main__":
    n = int(f())
    m = int(f())
    bus = []
    for i in range(m):
        bus.append(list(map(int, f().split())))
    print(bus)

    print(floyd(n, m, bus))
