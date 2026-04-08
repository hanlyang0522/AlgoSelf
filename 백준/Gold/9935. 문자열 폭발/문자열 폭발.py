import sys
from itertools import combinations
from collections import deque

f = sys.stdin.readline


def solve():
    s = input()
    bomb = input()

    dq = deque()

    for i in range(len(s)):
        dq.append(s[i])

        if s[i] == bomb[-1] and len(dq) >= len(bomb):
            # 뺄 수 있는지 체크
            tmp = deque()
            # flag = True

            for j in range(len(bomb)):
                t = dq.pop()
                tmp.append(t)

                if t != bomb[-1 - j]:
                    # flag = False

                    while tmp:
                        dq.append(tmp.pop())
                    break

    if not dq:
        print("FRULA")
    else:    
        while dq:
            print(dq.popleft(), end='')
        print()

    pass


if __name__ == "__main__":
    solve()
