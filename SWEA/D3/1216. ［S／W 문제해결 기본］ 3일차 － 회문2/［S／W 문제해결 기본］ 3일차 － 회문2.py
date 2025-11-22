T = 10


def isPalin(s: str):
    if s == s[::-1]:
        return True
    else:
        return False


for tc in range(1, T + 1):
    t = int(input())
    mat = [list(map(str, input())) for _ in range(100)]

    max_l = 1

    for y in range(100):
        for l in range(2, 101):
            for x in range(101 - l):
                s = ''.join(mat[y][x:x + l])

                if isPalin(s):
                    max_l = max(max_l, l)
                    break

    mat_trans = list(map(list, zip(*mat)))

    for y in range(100):
        for l in range(2, 101):
            for x in range(101 - l):
                s = ''.join(mat_trans[y][x:x + l])

                if isPalin(s):
                    max_l = max(max_l, l)
                    break

    print(f"#{t} {max_l}")
