import sys
import copy

f = sys.stdin.readline

dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]

N = int(f())
graph = [[] for i in range(N)]
max_h = 0

for i in range(N):
    graph[i] = list(map(int, f().split()))
    max_h = max(max_h, max(graph[i]))

max_island = 0
for rain in range(max_h):
    cnt = 0
    queue = []
    graph_copy = copy.deepcopy(graph)

    for i in range(N):  # y
        for j in range(N):  # x
            if graph_copy[i][j] - rain > 0:
                cnt += 1
                graph_copy[i][j] = 0
                queue.append([i, j])

                while queue:
                    _i, _j = queue.pop()

                    for dy, dx in dir:
                        if _j + dx < 0 or _j + dx >= N or _i + dy < 0 or _i + dy >= N:
                            continue
                        if graph_copy[_i + dy][_j + dx] - rain > 0:
                            graph_copy[_i + dy][_j + dx] = 0
                            queue.append([_i + dy, _j + dx])

    # print(cnt)
    max_island = max(max_island, cnt)

print(max_island)
