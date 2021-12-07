from itertools import combinations


def solution(relation):
    global n_row
    global n_col
    n_row, n_col = len(relation), len(relation[0])

    ans = 0

    num_list = [x for x in range(n_col)]
    comb_list = []

    # 모든 조합 생성
    for i in range(1, n_col + 1):
        for j in combinations(num_list, i):
            comb_list.append(j)

    for c in comb_list:
        if c == -1:
            continue

        # 유일성 만족할 경우
        if ifUnique(relation, c):
            ans += 1

            # 중복 요소 제거
            for sub_c in comb_list[:]:
                if sub_c == -1:
                    continue
                if ifIn(c, sub_c):
                    comb_list[comb_list.index(sub_c)] = -1

    # print(ans)
    return ans


def ifUnique(relation, canKey):
    subDB = [[relation[row][col] for col in canKey] for row in range(n_row)]

    for i in range(n_row):
        for j in range(i + 1, n_row):
            if subDB[i] == subDB[j]:
                return False
    return True


def ifIn(gt, target):
    for g in gt:
        if g not in target:
            return False
    return True


solution(
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
)

solution(
    [
        ["a", "1", "aaa", "c", "ng"],
        ["a", "1", "bbb", "e", "g"],
        ["c", "1", "aaa", "d", "ng"],
        ["d", "2", "bbb", "d", "ng"],
    ]
)

solution(
    [
        ["100", "100", "ryan", "music", "2"],
        ["200", "200", "apeach", "math", "2"],
        ["300", "300", "tube", "computer", "3"],
        ["400", "400", "con", "computer", "4"],
        ["500", "500", "muzi", "music", "3"],
        ["600", "600", "apeach", "music", "2"],
    ]
)
