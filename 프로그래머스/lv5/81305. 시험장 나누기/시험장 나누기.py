"""
답 범위 정해두고 parametric search 사용
"""

import sys

sys.setrecursionlimit(10**6)

# 좌우 자식 노드
l = [0 for _ in range(10005)]
r = [0 for _ in range(10005)]
# 응시 인원
x = [0 for _ in range(10005)]
# 부모 노드
p = [-1 for _ in range(10005)]

# 노드 수, 루트, 그룹 수
n = 0
root = 0
cnt = 0


def dfs(curNode, maxCnt):
    global cnt

    # 양 트리에서 올라오는 인원 수
    lv = 0
    if l[curNode] != -1:
        lv = dfs(l[curNode], maxCnt)
    rv = 0
    if r[curNode] != -1:
        rv = dfs(r[curNode], maxCnt)

    # 1. 모두 합해도 maxCnt 이하일 경우
    if x[curNode] + lv + rv <= maxCnt:
        return x[curNode] + lv + rv

    # 2. 둘 중 작은것을 합해 maxCnt 이하일 경우
    if x[curNode] + min(lv, rv) <= maxCnt:
        cnt += 1  # 둘 중 큰 인원은 그룹을 지어버림
        return x[curNode] + min(lv, rv)

    # 3. 둘 다 아닐 경우(양쪽 다 자를 경우)
    cnt += 2

    return x[curNode]


def solve(maxPpl):
    global cnt

    cnt = 0
    dfs(root, maxPpl)
    cnt += 1  # 남은 인원으로 만든 그룹

    return cnt


def solution(k, num, links):
    global root

    n = len(num)

    # 트리 초기화
    for i in range(n):
        l[i], r[i] = links[i]
        x[i] = num[i]
        if l[i] != -1:
            p[l[i]] = i
        if r[i] != -1:
            p[r[i]] = i

    # root 노드 찾기
    for i in range(n):
        if p[i] == -1:
            root = i
            break

    start = max(x)
    end = 10**8
    while start < end:
        mid = (start + end) // 2
        if solve(mid) <= k:
            end = mid
        else:
            start = mid + 1

    return start