"""

"""

import sys

f = sys.stdin.readline

dice = [4, 5, 1, 2, 6, 3]


def roll(dir):
    if dir == 0:
        dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]
    elif dir == 1:
        dice[0], dice[2], dice[5], dice[4] = dice[4], dice[0], dice[2], dice[5]
    else:
        dice[1], dice[2], dice[3], dice[4] = dice[4], dice[1], dice[2], dice[3]


def solve(r, c):
    ans = 0
    quo, rem = (c - 1) // 4, (c - 1) % 4
    dirLR = 1  # 0:L, 1:R

    for i in range(r):
        ans += dice[2]
        ans += quo * (dice[0] + dice[2] + dice[4] + dice[5])

        for j in range(rem):
            roll(dirLR)
            ans += dice[2]

        if dirLR == 1:
            dirLR = 0
        else:
            dirLR = 1

        roll(2)

    print(ans)


if __name__ == "__main__":
    r, c = map(int, f().split())

    solve(r, c)
