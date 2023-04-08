"""
구현
"""

dirs = [
    (0, -1),
    (
        -1,
        -1,
    ),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
]
diags = [
    (
        -1,
        -1,
    ),
    (-1, 1),
    (1, 1),
    (1, -1),
]

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

    for _ in range(m):
        d, s = map(int, input().split())
        cMoved = []

        for cy, cx in clouds:
            # 1. 이동
            dy, dx = dirs[d - 1][0] * s, dirs[d - 1][1] * s
            cy, cx = (cy + dy + n) % n, (cx + dx + n) % n
            cMoved.append((cy, cx))

            # 23. 비 + 사라짐
            mat[cy][cx] += 1

        # 4. 물 복사
        for cy, cx in cMoved:
            for dy, dx in diags:
                ty, tx = cy + dy, cx + dx

                if 0 <= ty < n and 0 <= tx < n and mat[ty][tx] > 0:
                    mat[cy][cx] += 1

        # 5. 구름 생성
        clouds = []
        for y in range(n):
            for x in range(n):
                if mat[y][x] >= 2 and (y, x) not in cMoved:
                    mat[y][x] -= 2
                    clouds.append((y, x))

    ans = 0
    for _ in range(n):
        ans += sum(mat[_])
    print(ans)
