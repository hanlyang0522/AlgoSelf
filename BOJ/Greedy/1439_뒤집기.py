import sys

f = sys.stdin.readline


def flip(num):
    cnt = 0
    prev = "?"

    for i in num:
        if i != prev:
            prev = i
            cnt += 1

    print((cnt) // 2)


if __name__ == "__main__":
    num = f()
    flip(num[:-1])
