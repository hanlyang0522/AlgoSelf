"""

"""

import sys

f = sys.stdin.readline


def solve(n, m, b):
    mat = []

    maxH = -1
    minH = sys.maxsize
    sumH = b

    for _ in range(n):
        tmp = list(map(int, f().split()))

        mat.append(tmp)

        maxH = max(maxH, max(tmp))
        minH = min(minH, min(tmp))
        sumH += sum(tmp)

    avgH = sumH // (n * m)
    # print(mat, maxH, sumH, avgH)

    totalTime = sys.maxsize
    totalH = -1

    for H in range(minH, avgH + 1):
        tmpTime = 0

        for y in range(n):
            for x in range(m):
                if mat[y][x] > H:
                    tmpTime += (mat[y][x] - H) * 2
                else:
                    tmpTime += H - mat[y][x]

        if tmpTime <= totalTime:
            totalTime = tmpTime
            totalH = H

    print(totalTime, totalH)


if __name__ == "__main__":
    n, m, b = map(int, f().split())

    solve(n, m, b)
