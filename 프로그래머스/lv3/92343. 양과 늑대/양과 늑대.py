"""
1. bfs/dfs로 매번 양/늑 체크하면서 돌리면 될듯?
2. 근데 현재 안 간 node도 다음에 갈 수 있으니 일단 저장해둬야할듯
3. 단순 bfs로 하니 양으로 가는/안가는 늑대길을 구분을 못하는 문제가 발생
4. togo에 (양-늑)수치를 같이 저장?
4-1. 아니면 각 양까지의 거리를 저장?

--> dfs가 구현이 더 편리, 완탐으로 해결 가능
--> 비재귀로 하니 경우의수가 한 선택지로 고정된다는 문제가 발생, 
재귀로 바꿔서 해결하기로 --> dfs로 해야됨! bfs는 재귀 불가
"""


def solution(info, edges):
    visit = [False for _ in range(len(info))]
    visit[0] = True
    sheeps = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            sheeps.append(sheep)
        else:
            return

        for i in range(len(edges)):
            p, c = edges[i]
            is_wolf = info[c]

            if visit[p] and not visit[c]:
                visit[c] = True
                dfs(sheep + (is_wolf == 0), wolf + (is_wolf == 1))
                visit[c] = False

    dfs(1, 0)

    return max(sheeps)