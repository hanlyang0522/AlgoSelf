import sys
import heapq

f = sys.stdin.readline

V, E = map(int, f().split())
start = int(f())
graph = [[sys.maxsize if i != j else 0 for i in range(V)] for j in range(V)]
# visited = [0 for i in range(V)]

for _ in range(E):
    u, v, w = map(int, f().split())
    if w < graph[u - 1][v - 1]:
        graph[u - 1][v - 1] = w

print(graph)


for i in range(V):
    print(graph[start][i])
