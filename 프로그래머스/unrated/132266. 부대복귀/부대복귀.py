'''
매 start맏 dest까지 탐색하는 것이 아니라 dest부터 역으로 모든 node 탐색!
'''

from collections import deque, defaultdict


def bfs(n, start, sources):
    q = deque([start])
    minCost = [-1 for _ in range(n + 1)]
    minCost[start] = 0

    while q:
        now = q.popleft()
        for next in rInfo[now]:
            if minCost[next] == -1:
                minCost[next] = minCost[now] + 1
                q.append(next)
                
    return [minCost[s] for s in sources]


def solution(n, roads, sources, destination):
    global rInfo
    
    rInfo = defaultdict(list)
    for a, b in roads:
        rInfo[a].append(b)
        rInfo[b].append(a)

    return bfs(n, destination, sources)