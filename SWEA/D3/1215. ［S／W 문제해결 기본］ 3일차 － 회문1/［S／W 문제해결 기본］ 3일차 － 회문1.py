T = 10


def isPalindrome(s: str):
    if s == s[::-1]:
        return 1
    else:
        return 0


for tc in range(1, T + 1):
    N = int(input())

    mat = []

    for _ in range(8):
        mat.append(list(input()))

    total = 0

    for y in range(8):
        for x in range(8 - N + 1):
            hor = mat[y][x:x + N]
            total += isPalindrome(hor)

    for x in range(8):
        for y in range(8 - N + 1):
            ver = []

            for z in range(y, y + N):
                ver.append(mat[z][x])

            total += isPalindrome(ver)

    print(f"#{tc} {total}")
