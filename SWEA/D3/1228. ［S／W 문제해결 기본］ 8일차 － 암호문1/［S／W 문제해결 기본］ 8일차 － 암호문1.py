T = 10


def recur(n, d, t):
    if d == t:
        return 1

    return n * recur(n, d + 1, t)


for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    N_c = int(input())
    c = input()
    commands = c.split('I ')
    commands.remove('')

    for comm in commands:
        co = list(comm.split(' '))
        x, y, s = int(co[0]), int(co[1]), co[2:-1]

        for i in range(y):
            li.insert(x, int(s[-(i+1)]))


    s = ''

    for i in range(10):
        s += ' ' + str(li[i])

    print(f"#{tc}{s}")
