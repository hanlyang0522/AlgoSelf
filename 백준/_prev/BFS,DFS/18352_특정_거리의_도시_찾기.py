# 그래프 한 노드에서 최단거리 --> 다익스트라 --> queue
from dis import dis
import sys
import heapq
from collections import defaultdict

f = sys.stdin.readline


def dijkstra(graph, cities, start, min_dist):
    Q = [(0, start)]  # (거리, node) 순서
    distance = [-1 for _ in range(cities + 1)]

    while Q:
        dist, node = heapq.heappop(Q)

        if distance[node] == -1:
            distance[node] = dist

            for v in graph[node]:
                update = dist + 1
                heapq.heappush(Q, (update, v))

    flag = False
    for i in range(1, cities + 1):
        if distance[i] == min_dist:
            flag = True
            print(i)
    if not flag:
        print(-1)


if __name__ == "__main__":
    N, M, K, X = map(int, f().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, f().split())
        graph[a].append(b)

    dijkstra(graph, N, X, K)
