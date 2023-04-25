"""
union-find
"""

import sys

sys.setrecursionlimit(1000000)

f = sys.stdin.readline


def find(parent, a):
    if a != parent[a]:
        parent[a] = find(parent, parent[a]) # 경로압축 하지 않을 경우 O(N^2)
    return parent[a]


def union(parent, a, b):
    x, y = find(parent, a), find(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


if __name__ == "__main__":
    n, m = map(int, f().split())
    parent = [i for i in range(n + 1)]

    for _ in range(m):
        c, a, b = map(int, f().split())
        if c == 0:
            union(parent, a, b)
        else:
            if find(parent, a) == find(parent, b):
                print("yes")
            else:
                print("no")
