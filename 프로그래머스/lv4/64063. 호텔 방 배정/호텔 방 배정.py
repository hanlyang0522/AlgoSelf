"""
union-find
k = 10^12, n = 2 * 10^5 --> NlogN으로 해결 가능
"""
import sys

sys.setrecursionlimit(int(1e9))


def find(x):
    global parent

    if parent.get(x) == None:
        parent[x] = x + 1
        return x
    else:
        parent[x] = find(parent.get(x))
        return parent.get(x)


def solution(k, room_number):
    global parent

    parent = dict()

    ans = [0 for _ in range(len(room_number))]
    for i in range(len(room_number)):
        ans[i] = find(room_number[i])

    return ans
