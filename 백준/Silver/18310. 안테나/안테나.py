# n = 1e5 --> O(n^2)는 시간초과
#
import sys

f = sys.stdin.readline


def anTennae(n, house):
    return house[(n - 1) // 2]


if __name__ == "__main__":
    n = int(f())
    house = list(map(int, f().split()))
    house.sort()

    print(anTennae(n, house))
