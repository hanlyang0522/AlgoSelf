# DFS에서 방향전환 시 방향전환 가능한지 check
# 현재 방향

import sys
from collections import deque

f = sys.stdin.readline


def move(p1, p2, nboard):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    poss = []  # 이동 가능한 위치

    # 상하좌우로 이동 가능
    for dy, dx in dirs:
        # 이동 후 위치
        n1 = (p1[0] + dy, p1[1] + dx)
        n2 = (p2[0] + dy, p2[1] + dx)
        if nboard[n1[0]][n1[1]] == 0 and nboard[n2[0]][n2[1]] == 0:
            poss.append((n1, n2))

    # 회전
    if p1[0] == p2[0]:  # 수평일 경우
        for i in [-1, 1]:
            if nboard[p1[0] + i][p1[1]] == 0 and nboard[p2[0] + i][p2[1]] == 0:  # 둘 다 0이어야 회전 가능
                poss.append((p1, (p1[0] + i, p1[1])))  # p1 기준 회전
                poss.append((p2, (p2[0] + i, p2[1])))  # p2 기준 회전
    else:  # 수직일 경우
        for i in [-1, 1]:
            if nboard[p1[0]][p1[1] + i] == 0 and nboard[p2[0]][p2[1] + i] == 0:  # 둘 다 0이어야 회전 가능
                poss.append(((p1[0], p1[1] + i), p1))  # p1 기준 회전
                poss.append(((p2[0], p2[1] + i), p2))  # p2 기준 회전

    return poss


def solution(board):
    # 가장자리 벽이 있는 보드 생성
    l = len(board)
    nboard = [[1] * (l + 2) for _ in range(l + 2)]
    for i in range(l):
        for j in range(l):
            nboard[i + 1][j + 1] = board[i][j]

    dq = deque([((1, 1), (1, 2), 0)])  # 리스트에 p1, p2, 경과시간 저장
    visit = set([((1, 1), (1, 2))])  # 지나온 위치 저장

    while dq:
        p1, p2, time = dq.popleft()
        if p1 == (l, l) or p2 == (l, l):
            return time

        # BFS
        for k in move(p1, p2, nboard):
            if k not in visit:
                dq.append((*k, time + 1))
                visit.add(k)


if __name__ == "__main__":
    print(
        solution(
            [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
        )
    )
