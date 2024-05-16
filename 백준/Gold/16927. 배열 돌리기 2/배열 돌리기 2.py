import sys

f = sys.stdin.readline


def solve(r, c, T):
    global mat

    mat = [list(map(int, f().split())) for _ in range(r)]

    for shell in range(min(r, c) // 2):
        cycle = (r - shell * 2 + c - shell * 2) * 2 - 4
        rot = T % cycle

        sY, sX = shell, shell
        eY, eX = r - 1 - shell, c - 1 - shell

        rotate(sY, sX, eY, eX, rot)

    for y in range(r):
        for x in range(c):
            print(mat[y][x], end=" ")
        print()


def rotate(sY, sX, eY, eX, rot):
    tmp = []
    tmp.extend(mat[sY][sX:eX])
    tmp.extend(mat[i][eX] for i in range(sY, eY))
    tmp.extend(mat[eY][i] for i in range(eX, sX, -1))
    tmp.extend(mat[i][sX] for i in range(eY, sY, -1))

    tmp = tmp[rot:] + tmp[:rot]  # rotate

    idx = 0

    for i in range(sX, eX):
        mat[sY][i] = tmp[idx]
        idx += 1

    for i in range(sY, eY):
        mat[i][eX] = tmp[idx]
        idx += 1

    for i in range(eX, sX, -1):
        mat[eY][i] = tmp[idx]
        idx += 1

    for i in range(eY, sY, -1):
        mat[i][sX] = tmp[idx]
        idx += 1


if __name__ == "__main__":
    r, c, T = map(int, f().split())

    solve(r, c, T)
