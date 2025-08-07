# 1. DFS
# 2. chile가 not 유망이면 parent도 not 유망

import sys


def isPossible(n):
    # 현재 node 기준 상위 row를 모두 검사
    for i in range(n):
        # 위, 대각선에 위치할 경우
        if board[i] == board[n] or abs(board[i] - board[n]) == (n - i):
            return False
    return True


def dfs(row):
    # 현재 row가 체스판을 넘어갔을 경우
    if row == N:
        global cnt
        cnt += 1

    else:
        for i in range(N):
            # 이미 퀸이 있는 row는 pass
            if visit[i]:
                continue

            # (row,i)에 퀸 올림
            board[row] = i

            # 유망한 node 검토
            if isPossible(row):
                # 현재 node의 하위 node에서 dfs
                visit[i] = True
                dfs(row + 1)
                visit[i] = False


if __name__ == "__main__":
    f = sys.stdin.readline
    N = int(f())
    cnt = 0
    board = [0 for _ in range(N)]
    visit = [False for _ in range(N)]

    dfs(0)
    print(cnt)
