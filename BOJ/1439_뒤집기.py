import sys
from collections import deque

f = sys.stdin.readline


def flip(num):
    li = []
    t_cnt = 1

    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            t_cnt += 1
        else:
            li.append([t_cnt, num[i]])
            t_cnt = 1
    # print(li)

    cnt = 0
    # while len(li)>1:
    l = len(li)
    cnt = l // 2
    if l % 2 == 0:
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    num = f()
    flip(num)
