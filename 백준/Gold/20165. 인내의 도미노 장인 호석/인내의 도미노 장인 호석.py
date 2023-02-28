import sys

dirs = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}


def attack(y, x, d):
    if not fallen[y][x]:
        return 0

    cnt = 1
    crash = mat[y][x] - 1
    fallen[y][x] = 0
    ny, nx = y, x
    dy, dx = dirs[d]
    while crash:
        crash -= 1
        ny += dy
        nx += dx
        if not (0 <= ny < n and 0 <= nx < m):
            break

        if fallen[ny][nx] == 1:
            fallen[ny][nx] = 0
            crash = max(crash, mat[ny][nx] - 1)
            cnt += 1

    return cnt


def defense(y, x):
    fallen[y][x] = 1


if __name__ == "__main__":
    f = sys.stdin.readline

    n, m, r = map(int, f().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, f().split())))
    fallen = [[1 for _ in range(m)] for __ in range(n)]

    score = 0
    for _ in range(r):
        y, x, d = f().split()
        score += attack(int(y) - 1, int(x) - 1, d)
        y, x = map(int, f().split())
        defense(y - 1, x - 1)

    print(score)
    for y in range(n):
        for x in range(m):
            print("S" if fallen[y][x] else "F", end="")
            if x != m - 1:
                print(" ", end="")
        print()
