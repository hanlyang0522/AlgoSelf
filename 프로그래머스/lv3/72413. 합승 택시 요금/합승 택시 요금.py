from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(n, graph, start):
    dist = {node: int(1e9) for node in range(1, n + 1)}
    dist[start] = 0

    q = []
    heappush(q, [dist[start], start])  # 비용, node 순 입력

    while q:
        curDist, curNode = heappop(q)

        if dist[curNode] < curDist:  # 기존 경로보다 비싸면 skip
            continue

        for newNode, newDist in graph[curNode].items():  # dict에선 node:비용으로 나옴
            di = curDist + newDist
            if di < dist[newNode]:  # 기존 경로보다 싸면 갱신
                dist[newNode] = di
                heappush(q, [di, newNode])
    return dist


def solution(n, s, a, b, fares):
    # graph 생성
    graph = defaultdict(dict)
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    # print(graph)

    # 다익스트라로 각 node간 최단 거리를 구함
    shortPath = {}
    for i in [s, a, b]:
        shortPath[i] = dijkstra(n, graph, i)
    # print(shortPath)

    # 각 node별 분기점일 경우의 최단 거리 구함
    ans = int(1e9)
    for i in range(1, n + 1):
        ans = min(
            ans,
            (shortPath[s][i] + shortPath[a][i] + shortPath[b][i]),
        )

    return ans