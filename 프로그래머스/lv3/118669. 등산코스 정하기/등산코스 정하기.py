import sys
from collections import deque, defaultdict


def solution(n, paths, gates, summits):
    ans = [0, 10000001]
    summits.sort()
    summits = set(summits)

    # 인접리스트 생성
    adjlist = defaultdict(list)
    for a, b, w in paths:
        adjlist[a].append([b, w])
        adjlist[b].append([a, w])

    # 게이트 상관없이 도달할 수 있는 최소 intensity 저장
    dist = [10000001 for _ in range(n + 1)]
    for gate in gates:
        dist[gate] = 0

    # 모든 출입구 큐에 삽입
    q = deque(gates)
    while q:
        curr = q.popleft()
        if curr in summits:
            continue

        for next, w in adjlist[curr]:
            if dist[next] > max(dist[curr], w):  # 더 적은 수로 방문할 수 있을 경우
                q.append(next)
                dist[next] = max(dist[curr], w)


    for summit in summits:
        if ans[1] > dist[summit]:
            ans[0] = summit
            ans[1] = dist[summit]
        elif ans[1] == dist[summit] and ans[0] > summit:
            ans[0] = summit

    return ans
