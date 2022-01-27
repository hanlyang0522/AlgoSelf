# DFS에서 방향전환 시 방향전환 가능한지 check
# 현재 방향

from re import L
import sys
from collections import deque

f = sys.stdin.readline

dlist = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def solution(board):
    N = len(board)
    time = [[-1 for i in range(N)] for j in range(N)]

    stk = deque()
    stk.append([0, 0, "L", "H", 0])  # y, x, 진행방향 L/D, 로봇방향 H/V, 경과시간

    while stk:
        y, x, m_dir, r_dir, time = stk.pop()

        for dy, dx in dlist:
            ty, tx = y + dy, x + dx

            if ty < 0 or ty > N - 1 or tx < 0 or tx > N - 1:
                continue
            elif board[ty][tx] == 1:
                continue

            if ty != 0:  # 이번 방향
                t_dir = "L"
            else:
                t_dir = "D"

            if t_dir != m_dir:
            # 돌릴 수 있는지 확인 후 돌리기
                pass
            else:
                


            # 진행한 곳이 더 느리면 skip, 빠르면 갱신 후 push

            

    return answer


if __name__ == "__main__":
    print(
        solution(
            [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
        )
    )
