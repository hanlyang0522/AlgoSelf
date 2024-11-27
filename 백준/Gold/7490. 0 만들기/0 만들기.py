"""

"""

import sys

f = sys.stdin.readline


def rec(end, curr, s):

    if curr == end + 1:
        if eval(s.replace(" ", "")) == 0:
            print(s)

        return

    rec(end, curr + 1, s + " " + str(curr))
    rec(end, curr + 1, s + "+" + str(curr))
    rec(end, curr + 1, s + "-" + str(curr))

    return


def solve(n):
    rec(n, 2, "1")

    return


if __name__ == "__main__":
    T = int(f())

    for i in range(T):
        solve(int(f()))
        print()
