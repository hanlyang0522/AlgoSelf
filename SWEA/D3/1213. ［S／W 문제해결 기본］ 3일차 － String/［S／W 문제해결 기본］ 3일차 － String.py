T = 10

for tc in range(1, T + 1):
    N = int(input())
    WORD = str(input())
    STR = str(input())

    cnt = STR.count(WORD)

    print(f"#{tc} {cnt}")
