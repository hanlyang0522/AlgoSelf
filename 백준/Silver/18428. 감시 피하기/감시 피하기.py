#
#
import sys

f = sys.stdin.readline
from itertools import combinations
from copy import deepcopy

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def isSeen(n, li, t):
    for dy, dx in dir:
        y, x = t

        while True:
            y += dy
            x += dx

            if 0 <= y < n and 0 <= x < n:
                if li[y][x] == "O":
                    break
                if li[y][x] == "S":
                    return True
            else:
                break

    return False


def isValid(n, li):
    comb = list(combinations(range(n * n), 3))
    teacher = []
    for i in range(n):
        for j in range(n):
            if li[i][j] == "T":
                teacher.append([i, j])

    for co in comb:
        li2 = deepcopy(li)

        # 장애물 세우기
        flag = False
        for c in co:
            y, x = c // n, c % n
            if li2[y][x] != "X":
                flag = True
                break
            li2[y][x] = "O"

        if flag:
            continue

        # 감시 피하는지 검사
        flag2 = False
        for t in teacher:
            if isSeen(n, li2, t):
                flag2 = True
                break

        if not flag2:
            return "YES"

    return "NO"


if __name__ == "__main__":
    n = int(f())
    li = []
    for _ in range(n):
        li.append(list(f().split()))

    print(isValid(n, li))
