"""
간단한 구현 문제
"""

import sys
from collections import defaultdict

f = sys.stdin.readline


def IsInRow(li):
    li = sorted(li)

    for i in range(len(li) - 1):
        if li[i] - li[i + 1] != -1:
            return False
    return True


def CalcCardScore():
    colors = defaultdict(list)
    digits = defaultdict(list)
    _digits = []

    for _ in range(5):
        c, d = f().split()
        colors[c].append(int(d))
        digits[d].append(c)
        _digits.append(int(d))

    colors = sorted(colors.items(), key=lambda x: -len(x[1]))
    digits = sorted(digits.items(), key=lambda x: -len(x[1]))
    score = 0

    if len(colors[0][1]) == 5 and IsInRow(colors[0][1]):
        score = max(colors[0][1]) + 900
    elif len(digits[0][1]) == 4:
        score = int(digits[0][0]) + 800
    elif len(digits[0][1]) == 3 and len(digits[1][1]) == 2:
        score = int(digits[0][0]) * 10 + int(digits[1][0]) + 700
    elif len(colors[0][1]) == 5:
        score = max(colors[0][1]) + 600
    elif IsInRow(_digits):
        score = max(_digits) + 500
    elif len(digits[0][1]) == 3:
        score = int(digits[0][0]) + 400
    elif len(digits[0][1]) == 2 and len(digits[1][1]) == 2:
        score = (
            max(int(digits[0][0]), int(digits[1][0])) * 10
            + min(int(digits[0][0]), int(digits[1][0]))
            + 300
        )
    elif len(digits[0][1]) == 2:
        score = int(digits[0][0]) + 200
    else:
        score = max(_digits) + 100

    print(score)


if __name__ == "__main__":
    CalcCardScore()
