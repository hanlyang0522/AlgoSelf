import sys

f = sys.stdin.readline

N, M = map(int, f().split())  # node, vertex

graph = [[0 for i in range(N)] for j in range(N)]
visit = [0 for i in range(N)]
queue = []

for i in range(M):
    u, v = map(int, f().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1

cnt = 0
for i in range(N):
    if visit[i] == 0:
        cnt += 1
        visit[i] = 1
        queue.append(i)

        while queue:
            node = queue.pop()
            visit[node] = 1

            for j in range(N):
                if graph[node][j] == 1:
                    if visit[j] == 0:
                        visit[j] = 1
                        queue.append(j)

print(cnt)
