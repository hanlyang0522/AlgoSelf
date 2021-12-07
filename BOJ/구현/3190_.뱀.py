import sys

f = sys.stdin.readline


def Dummy():
    apple = []
    dir = []

    N = int(f())
    K = int(f())
    for _ in range(K):
        apple.append(list(map(int, f().split())))
    L = int(f())
    for _ in range(L):
        d1, d2 = f().split()
        dir.append([int(d1), d2])

    print(apple)
    print(dir)

    mat = [[0] * N for _ in range(N)]
    for y, x in apple:
        mat[y - 1][x - 1] = 1
    mat[0][0] = -1

    cnt = 0
    while True:



if __name__ == "__main__":

    Dummy()
