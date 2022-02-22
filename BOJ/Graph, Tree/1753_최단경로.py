# 모든 가중치가 양수 & 방향 그래프 --> Dijkstra

import sys
import heapq
from collections import defaultdict


def Dijkstra(graph, V, start):
    Q = [(0, start)]  # (거리, node)로 queue 생성
    distance = [-1 for _ in range(V + 1)]  # 방문 및 거리 체크

    while Q:
        dist, node = heapq.heappop(Q)  # 현재 node와 총 거리
        if distance[node] == -1:  # 방문하지 않았을 경우
            distance[node] = dist  # 방문 체크
            for v, w in graph[node]:  # 현재 node와 연결된 node에 대해
                update = dist + w  # 상대 node와 가는데 걸리는 총 거리 push
                heapq.heappush(Q, (update, v))

    for i in range(1, V + 1):
        if i == start:
            print("0")
        elif distance[i] == -1:
            print("INF")
        else:
            print(distance[i])


f = sys.stdin.readline

V, E = map(int, f().split())
start = int(f())
graph = defaultdict(list)  # 그래프 생성

for _ in range(E):
    u, v, w = map(int, f().split())
    graph[u].append((v, w))

Dijkstra(graph, V, start)
