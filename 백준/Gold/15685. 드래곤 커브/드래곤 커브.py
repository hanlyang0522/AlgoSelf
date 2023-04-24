"""
구현
"""

import sys

f = sys.stdin.readline

dirs = ((0, 1), (-1, 0), (0, -1), (1, 0))
mat = [[0 for _ in range(101)] for __ in range(101)]


def dragonCurve(x, y, d, _g):
    global mat

    mat[y][x] = 1
    mli = [d]  # 절대경로가 아니라 방향만 저장하면 됨

    for g in range(_g):
        # mli에 있는 역순으로 90도 회전해서 이동
        for md in mli[::-1]:
            # 90도 회전 + 이동경로 저장
            mli.append((md + 1) % 4)

    for md in mli:
        y, x = y + dirs[md][0], x + dirs[md][1]
        mat[y][x] = 1


if __name__ == "__main__":
    n = int(f())
    for _ in range(n):
        x, y, d, g = map(int, f().split())
        dragonCurve(x, y, d, g)

    cnt = 0
    for y in range(100):
        for x in range(100):
            if mat[y][x] and mat[y][x + 1] and mat[y + 1][x] and mat[y + 1][x + 1]:
                cnt += 1

    print(cnt)
