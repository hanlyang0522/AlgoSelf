"""
빡구현
"""

import sys
from collections import defaultdict

f = sys.stdin.readline

dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def move():
    global fbls
    di = defaultdict(list)

    # 파이어볼 이동
    for k, v in fbls.items():
        r, c = k
        for m, s, d in v:
            nr, nc = (r + s * dirs[d][0]) % n, (c + s * dirs[d][1]) % n
            di[(nr, nc)].append((m, s, d))

    fbls = defaultdict(list)

    for k, v in di.items():
        # 파이어볼 합체
        r, c = k
        if len(v) > 1:
            sumM, sumS = 0, 0
            tmpD = v[0][2] % 2
            flag = True
            for _m, _s, _d in v:
                sumM += _m
                sumS += _s
                if _d % 2 != tmpD:
                    flag = False

            # 파이어볼 분리
            m = sumM // 5
            if m == 0:
                continue
            s = int(sumS // len(v))
            if flag:
                d = [0, 2, 4, 6]
            else:
                d = [1, 3, 5, 7]
            for __d in d:
                fbls[(r, c)].append((m, s, __d))
        # 1개는 그대로 
        else:
            fbls[k].append(v[0])


if __name__ == "__main__":
    n, m, k = map(int, f().split())
    fbls = defaultdict(list)

    for _ in range(m):
        r, c, m, s, d = map(int, f().split())
        fbls[(r - 1, c - 1)].append((m, s, d))

    for _ in range(k):
        move()

    total = 0
    for k, v in fbls.items():
        for m, s, d in v:
            total += m
    print(total)
