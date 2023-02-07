def solution(n, build_frame):
    answer = [[]]
    li = [[0 for _ in range(n + 1)] for __ in range(n + 1)]  # 보=1 기둥=2 없음=0

    for x, y, a, b in build_frame:
        if a:  # 보
            if b:  # 설치
                li[y][x] += 1
            else:  # 삭제
                li[y][x] -= 1
        else:  # 기둥
            if b:
                if y == 0 or li[y - 1][x] >= 2 or :
                    li[y][x] += 2
            else:
                li[y][x] -= 2
    return li


print(
    solution(
        5,
        [
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [2, 1, 0, 1],
            [2, 2, 1, 1],
            [5, 0, 0, 1],
            [5, 1, 0, 1],
            [4, 2, 1, 1],
            [3, 2, 1, 1],
        ],
    )
)
print(
    solution(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)
