T = int(input())

h = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(1, T + 1):
    R, C = map(int, input().split())

    SUM = 0
    origSUM = 0
    flag = False

    for y in range(R):
        mat = list(map(int, input()))

        if flag:
            continue

        STR = ''
        odd = True

        for idx in range(C - 1, -1, -1):
            if mat[idx] == 0:
                continue

            # 암호 시작
            for x in range(idx - 56 + 1, idx + 1):
                STR += str(mat[x])

                if len(STR) == 7:
                    num = h[STR]

                    if odd:
                        SUM += 3 * num
                        origSUM += num
                        odd = False
                    else:
                        SUM += num
                        origSUM += num
                        odd = True

                    STR = ''

            flag = True
            break

        if flag:
            if SUM % 10 != 0:
                origSUM = 0

    print(f"#{tc} {origSUM}")
