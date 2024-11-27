"""

"""

import sys

f = sys.stdin.readline


def solve(n):
    pattern = f()
    asterisk = pattern.find("*")

    pFront = pattern[:asterisk]
    pBack = pattern[asterisk + 1 : -1]
    pLen = len(pFront) + len(pBack)

    for i in range(n):
        file = f().strip()

        if file.startswith(pFront) and file.endswith(pBack) and len(file) >= pLen:
            print("DA")
        else:
            print("NE")


if __name__ == "__main__":
    n = int(f())

    solve(n)
