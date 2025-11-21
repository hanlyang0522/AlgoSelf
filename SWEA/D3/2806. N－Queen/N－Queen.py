T = int(input())


def isInLine(y1, x1, y2, x2):
    if abs(y1 - y2) == abs(x1 - x2) or y1 == y2 or x1 == x2:
        return True
    else:
        return False


def dfs(pos, visit: list):
    global total
    global N

    if len(visit) == N:
        total += 1
        return

    for t_pos in range(pos, N ** 2):
        ty, tx = t_pos // N, t_pos % N

        line_flag = True

        for vy, vx in visit:
            if isInLine(vy, vx, ty, tx):
                line_flag = False
                break

        if line_flag:
            visit.append((ty, tx))
            dfs(t_pos+1, visit)
            visit.pop()


for tc in range(1, T + 1):
    N = int(input())

    total = 0
    visit = []

    for i in range(N ** 2):
        y, x = i // N, i % N

        visit.append((y, x))
        dfs(i+1, visit)
        visit.pop()

    print(f"#{tc} {total}")
