import sys

f = sys.stdin.readline
N = int(f())

graph = []
for i in range(N):
    graph.append(list(map(int, f().split())))

bf = []

print(graph)
