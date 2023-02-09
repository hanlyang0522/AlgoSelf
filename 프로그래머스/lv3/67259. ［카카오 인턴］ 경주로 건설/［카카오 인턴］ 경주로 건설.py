"""
1. n = 25 -> bfs + 방향 이동마다 금액 추가
2. 단순 재귀bfs로 하니 정확도, 효율성 모두 실패
3. stack 써서 minCost 저장하는 matrix 따로 만들기?
--> 수정하니 정확성 80, 1개는 시간초과
4. 코드 수정 이후에도 테케25번이 계속 걸림.. 
--> 방향에 따라 다른 비용이 소요되기 때문에 dict를 사용해야함!
"""


from collections import deque


def solution(board):
    N = len(board)
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # r l d u
    ans = int(1e9)

    st = deque()
    st.append((0, 0, 0, -1))  # y, x, cost, dir
    visited = {  # y,x,dir: cost
        (0, 0, 0): 0,
        (0, 0, 1): 0,
        (0, 0, 2): 0,
        (0, 0, 3): 0,
    }
    while st:
        y, x, cost, dir = st.popleft()

        for d in range(4):
            ny, nx = y + dirs[d][0], x + dirs[d][1]

            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                if (dir - d) % 2 == 0 or dir == -1:  # 직진
                    newCost = cost + 100
                else:  # 코너
                    newCost = cost + 600

                if [ny, nx] == [N - 1, N - 1]:
                    ans = min(ans, newCost)
                elif visited.get((ny, nx, d)) is None or visited.get((ny, nx, d)) > newCost:
                    visited[(ny, nx, d)] = newCost
                    st.append((ny, nx, newCost, d))

    return ans