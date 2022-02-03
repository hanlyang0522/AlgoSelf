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
    # print(num, len(num))
    # cnt = 0
    # for i in range(len(num) - 1):
    #     if num[i] != num[i + 1]:
    #         cnt += 1
    # print((cnt + 1) // 2)


if __name__ == "__main__":
    num = f()
    flip(num[:-1])
