from collections import defaultdict


def dfs(start, mat, visit):
    stack = []
    stack.append(start)

    while stack:
        now = stack.pop()

        for next in mat[now]:
            if next not in visit:
                visit.append(next)
                stack.append(next)


def solution(n, computers):
    ans = 0
    mat = defaultdict(list)
    visit = []

    for i in range(n):
        for j in range(i, n):
            if computers[i][j]:
                mat[i].append(j)
                mat[j].append(i)

    for i in range(n):
        if i not in visit:
            ans += 1
            dfs(i, mat, visit)

    return ans
