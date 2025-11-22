T = 10


def recur(n, d, t):
    if d == t:
        return 1

    return n * recur(n, d + 1, t)


for tc in range(1, T + 1):
    t = int(input())
    n, t = map(int, input().split())

    num = recur(n, 0, t)

    print(f"#{tc} {num}")
