"""

"""

import sys

f = sys.stdin.readline


def solve(n, m, b):
    mat = [0] * 257

    for _ in range(n):
        for tmpH in map(int, f().split()):
            mat[tmpH] += 1

    totalTime = sys.maxsize
    totalH = -1

    for targetH in range(257):
        tmpTime = 0
        blockAdd, blockSub = 0, 0

        for tmpH in range(257):
            if mat[tmpH] == 0:
                continue

            if tmpH > targetH:
                blockSub += (tmpH - targetH) * mat[tmpH]
            else:
                blockAdd += (targetH - tmpH) * mat[tmpH]

        if blockAdd > blockSub + b:
            continue

        tmpTime = blockAdd + blockSub * 2

        if tmpTime <= totalTime:
            totalTime = tmpTime
            totalH = targetH

    print(totalTime, totalH)


if __name__ == "__main__":
    n, m, b = map(int, f().split())

    solve(n, m, b)
