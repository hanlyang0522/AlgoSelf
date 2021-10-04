def dfs(start, tree, parents):
    for i in tree[start]:  # 시작점과 연결된 모든 node
        if parents[i] == 0:  # 아직 방문하지 않았다면(parent가 없다면)
            parents[i] = start  # 현재node가 parent로
            dfs(i, tree, parents)  # 연결된 node에 대해 dfs


import sys

sys.setrecursionlimit(10 ** 9)
f = sys.stdin.readline

N = int(f())
tree = [[] for _ in range(N + 1)]  # 연결된 모든 node 저장
parent = [0 for _ in range(N + 1)]

for i in range(N - 1):
    n1, n2 = map(int, (f().split()))

    # 연결 node 양방향으로 저장
    tree[n1].append(n2)
    tree[n2].append(n1)

dfs(1, tree, parent)

for i in range(2, N + 1):
    print(parent[i])
