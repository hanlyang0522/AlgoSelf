"""
1. result mat 크기
45: r+c-1 * r+c-1 / 이외 홀수 모두
90: c * r / 270
180: r * c
"""

import sys

f = sys.stdin.readline


def solve(r, c):
    mat = [["0"] * c for _ in range(r)]

    for y in range(r):
        tmp = f()

        for x in range(c):
            mat[y][x] = tmp[x]

    for y in range(r - 2, -1, -1):
        for x in range(c):
            yNow = y
            yNext = y + 1

            if mat[yNow][x] != "o":
                continue

            while yNext <= r - 1 and mat[yNext][x] == ".":
                mat[yNow][x] = "."
                mat[yNext][x] = "o"

                yNow += 1
                yNext += 1

    for y in range(r):
        for x in range(c):
            print(mat[y][x], end="")
        print()


if __name__ == "__main__":
    r, c = map(int, f().split())

    solve(r, c)
