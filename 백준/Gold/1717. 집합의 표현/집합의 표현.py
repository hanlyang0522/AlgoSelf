"""
union-find
"""

import sys

sys.setrecursionlimit(1000000)

f = sys.stdin.readline


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a]) # 경로압축 하지 않을 경우 O(N^2)
    return parent[a]


def union(a, b):
    x, y = find(a), find(b)
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
            union(a, b)
        else:
            if find(a) == find(b):
                print("yes")
            else:
                print("no")
