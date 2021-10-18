import sys
from itertools import combinations

f = sys.stdin.readline


def solution(line):
    point = []
    xlist = []
    ylist = []

    comb = combinations(line, 2)
    for [A, B, E], [C, D, F] in comb:
        if A * D - B * C == 0:
            continue
        x = (B * F - E * D) / (A * D - B * C)
        y = (E * C - A * F) / (A * D - B * C)

        if x == int(x) and y == int(y):
            x, y = int(x), int(y)
            point.append([x, y])
            xlist.append(x)
            ylist.append(y)

    min_x, max_x, min_y, max_y = min(xlist), max(xlist), min(ylist), max(ylist)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    graph = [["." for i in range(width)] for j in range(height)]

    for [x, y] in point:
        graph[y - min_y][x - min_x] = "*"

    answer = []
    for i in range(height, 0, -1):
        answer.append("".join(graph[i - 1]))

    print(answer)
    return answer


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
solution([[1, -1, 0], [2, -1, 0]])
solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])
