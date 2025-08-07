import sys

f = sys.stdin.readline


def solution(sizes):
    max_l, max_s = 0, 0

    for l, s in sizes:
        if s > l:
            l, s = s, l

        max_l = max(max_l, l)
        max_s = max(max_s, s)

    print(max_l * max_s)
    return max_l * max_s


solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
