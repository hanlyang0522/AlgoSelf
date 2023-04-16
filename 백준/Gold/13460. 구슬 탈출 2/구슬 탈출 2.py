"""
구현
"""

import sys
from collections import deque, defaultdict

f = sys.stdin.readline

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(mat, rPos, bPos):
    q = deque()
    q.append((rPos, bPos, 0))
    visit = defaultdict(bool)

    while q:
        (_ry, _rx), (_by, _bx), cnt = q.popleft()

        # 10회 넘어가면 종료
        if cnt == 10:
            return -1

        for dy, dx in dirs:
            # 어느 공 먼저 이동할지 결정
            ry, rx = _ry, _rx
            rFirst = True
            while True:
                ry, rx = ry + dy, rx + dx
                if mat[ry][rx] == "#":
                    break
                elif (ry, rx) == (_by, _bx):
                    rFirst = False
                    break

            # 빨강 먼저 이동
            if rFirst:
                # 벽에 부딪힐 때까지 이동
                rFlag = False
                ry, rx = _ry, _rx
                while mat[ry + dy][rx + dx] != "#":
                    ry, rx = ry + dy, rx + dx
                    # 구멍에 빠질 경우
                    if mat[ry][rx] == "O":
                        ry, rx = -1, -1
                        rFlag = True
                        break

                bFlag = False  # 파랑이 빠지는지 검사
                by, bx = _by, _bx
                while mat[by + dy][bx + dx] != "#" and (by + dy, bx + dx) != (ry, rx):
                    by, bx = by + dy, bx + dx
                    if mat[by][bx] == "O":
                        bFlag = True
                        break

            # 파랑 먼저 이동
            else:
                bFlag = False  # 파랑이 빠지는지 검사
                by, bx = _by, _bx
                while mat[by + dy][bx + dx] != "#":
                    by, bx = by + dy, bx + dx
                    if mat[by][bx] == "O":
                        bFlag = True
                        break

                rFlag = False
                ry, rx = _ry, _rx
                while mat[ry + dy][rx + dx] != "#" and (ry + dy, rx + dx) != (by, bx):
                    ry, rx = ry + dy, rx + dx
                    # 구멍에 빠질 경우
                    if mat[ry][rx] == "O":
                        rFlag = True
                        break

            # 파랑이 구멍에 빠질 경우
            if bFlag:
                continue
            elif rFlag:
                return cnt + 1

            if not visit[(ry, rx, by, bx)]:
                visit[(ry, rx, by, bx)] = True
                q.append(((ry, rx), (by, bx), cnt + 1))

    return -1


if __name__ == "__main__":
    n, m = map(int, f().split())
    mat = []
    for y in range(n):
        tmp = list(f())

        for x in range(m):
            if tmp[x] == "B":
                tmp[x] = "."
                bPos = (y, x)
            elif tmp[x] == "R":
                tmp[x] = "."
                rPos = (y, x)

        mat.append(tmp[:-1])

    print(bfs(mat, rPos, bPos))
