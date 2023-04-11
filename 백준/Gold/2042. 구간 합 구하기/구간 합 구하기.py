"""
segment tree
"""

import sys

f = sys.stdin.readline


def update(idx, num):
    global tree, sIdx

    idx += sIdx
    tree[idx] = num
    idx /= 2

    while idx >= 1:
        idx = int(idx)
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        idx /= 2


def query(left, right):
    global tree, sIdx

    left += sIdx
    right += sIdx
    total = 0

    while left <= right:
        if left % 2 == 1:
            total += tree[left]
        if right % 2 == 0:
            total += tree[right]

        left = (left + 1) // 2
        right = (right - 1) // 2

    return total


if __name__ == "__main__":
    global sIdx, tree

    n, m, k = map(int, f().split())

    sIdx = 1
    while sIdx < n:
        sIdx *= 2

    tree = [0 for _ in range(sIdx * 2)]

    for i in range(n):
        update(i, int(f()))

    for i in range(m + k):
        a, b, c = map(int, f().split())

        if a == 1:
            update(b - 1, c)
        else:
            print(query(b - 1, c - 1))
