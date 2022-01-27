# 2중 리스트의 탐색을 2중 for문으로 하는 것보다
# deque로 변환하면 속도가 빨라짐? --> 경우에 따라 다른듯

import sys
from collections import deque

f = sys.stdin.readline


def pmove(N, L, R, mat):
    d_list = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    yx_list = deque(_ for _ in range(N * N))
    flag = True  # 연합 있는지 체크
    cnt = -1

    while flag:
        visit = [[False for i in range(N)] for j in range(N)]
        flag = False
        cnt += 1

        # for y in range(0, N):
        #     for x in range(0, N):
        for num in yx_list:
            y, x = num // N, num % N

            if visit[y][x]:
                continue
            stk = deque()  # DFS
            stk.append([y, x])
            visit[y][x] = True
            # 연합된 국가 담기
            union_pos = [[y, x]]
            union_ppl = mat[y][x]

            while stk:
                # BFS
                sty, stx = stk.popleft()

                for dy, dx in d_list:  # 근접 국가 중 연합 있는지 탐색
                    ty, tx = sty + dy, stx + dx

                    if ty < 0 or ty >= N or tx < 0 or tx >= N or visit[ty][tx]:
                        continue

                    if L <= abs(mat[sty][stx] - mat[ty][tx]) <= R:
                        stk.append([ty, tx])
                        visit[ty][tx] = True
                        union_pos.append([ty, tx])
                        union_ppl += mat[ty][tx]

            # print(unite_pos, unite_ppl)
            if len(union_pos) > 1:
                flag = True
                ppl = union_ppl // len(union_pos)
                for uy, ux in union_pos:
                    mat[uy][ux] = ppl

    return cnt


if __name__ == "__main__":
    N, L, R = map(int, f().split())
    mat = []
    for _ in range(N):
        mat.append(list(map(int, f().split())))

    if N == 1:
        print(0)
    else:
        print(pmove(N, L, R, mat))
