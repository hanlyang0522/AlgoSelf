"""
dfs or union-find
마지막에 그래프 개수 셀 때 i를 바로 찾는게 아니라 parent[i]를 기준으로 카운트해야함
"""
from collections import defaultdict


def find(x):
    global parent

    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global parent

    a, b = find(x), find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    global parent

    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j)

    di = defaultdict(int)
    for i in parent:
        di[find(i)] += 1

    return len(di.items())