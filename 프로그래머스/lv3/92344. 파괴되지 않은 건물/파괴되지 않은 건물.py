def solution(board, skill):
    w, h = len(board[0]), len(board)
    mat = [[0 for _ in range(w + 1)] for __ in range(h + 1)]
    # 턴 따라 진행
    for typ, r1, c1, r2, c2, deg in skill:
        # print(typ, r1, c1, r2, c2, deg)
        # 공격일 경우
        if typ == 1:
            deg *= -1
        # 누적합 저장
        mat[r1][c1] += deg
        mat[r1][c2 + 1] -= deg
        mat[r2 + 1][c1] -= deg
        mat[r2 + 1][c2 + 1] += deg

    # 열 누적
    for y in range(h):
        for x in range(1, w):
            mat[y][x] += mat[y][x - 1]

    # 열 누적
    for x in range(w):
        for y in range(1, h):
            mat[y][x] += mat[y - 1][x]

    # print(mat)

    # 건물 개수 카운트
    cnt = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] + mat[y][x] > 0:
                cnt += 1

    return cnt