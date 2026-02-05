import sys
from collections import deque

f = sys.stdin.readline


def rotate(li):
    return list(list(zip(*li[::-1])))


def solve():
    N, M, R = map(int, f().split())
    mat_orig = [list(map(int, f().split())) for _ in range(N)]
    Rlist = list(map(int, f().split()))

    result = [False, False, 0]  # 상하, 좌우, 회전각도(0123)
    orders = [0, 1, 3, 2]  # 각 사분면 순서

    for r in Rlist:
        if r == 1:
            if result[2] % 2:
                result[1] = not result[1]
            else:
                result[0] = not result[0]
            orders = [orders[2], orders[3], orders[0], orders[1]]
        elif r == 2:
            if result[2] % 2:
                result[0] = not result[0]
            else:
                result[1] = not result[1]
            orders = [orders[1], orders[0], orders[3], orders[2]]
        elif r == 3:
            result[2] = (result[2] + 1) % 4
            orders = [orders[2], orders[0], orders[3], orders[1]]
        elif r == 4:
            result[2] = (result[2] - 1) % 4
            orders = [orders[1], orders[3], orders[0], orders[2]]
        elif r == 5:
            orders = [orders[2], orders[0], orders[3], orders[1]]
        elif r == 6:
            orders = [orders[1], orders[3], orders[0], orders[2]]

    n, m = N // 2, M // 2
    mat_new = [
        [row[:m] for row in mat_orig[:n]],
        [row[m:] for row in mat_orig[:n]],
        [row[m:] for row in mat_orig[n:]],
        [row[:m] for row in mat_orig[n:]],
    ]

    # 상하 flip
    if result[0]:
        mat_new[0].reverse()
        mat_new[1].reverse()
        mat_new[2].reverse()
        mat_new[3].reverse()

    # 좌우 flip
    if result[1]:
        mat_new[0] = [row[::-1] for row in mat_new[0]]
        mat_new[1] = [row[::-1] for row in mat_new[1]]
        mat_new[2] = [row[::-1] for row in mat_new[2]]
        mat_new[3] = [row[::-1] for row in mat_new[3]]

    # 회전
    for _ in range(result[2]):
        mat_new[0] = rotate(mat_new[0])
        mat_new[1] = rotate(mat_new[1])
        mat_new[2] = rotate(mat_new[2])
        mat_new[3] = rotate(mat_new[3])

    # 결과 print
    top_result = []
    for row in range(len(mat_new[0])):
        top_result.append(mat_new[orders[0]][row] + mat_new[orders[1]][row])

    bot_result = []
    for row in range(len(mat_new[0])):
        bot_result.append(mat_new[orders[2]][row] + mat_new[orders[3]][row])

    total_result = top_result + bot_result

    for i in total_result:
        print(*i)


if __name__ == "__main__":
    solve()
