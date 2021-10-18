import sys

f = sys.stdin.readline

dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

while True:
    Width, Height = map(int, f().split())
    if Width == 0 and Height == 0:
        break
    graph = [[] for i in range(Height)]

    for i in range(Height):
        li = list(map(int, f().split()))
        graph[i] = li

    queue = []
    island = 0
    for w in range(Width):
        for h in range(Height):
            if graph[h][w] == 1:
                island += 1
                graph[h][w] = 0
                queue.append([h, w])

                while queue:
                    [_h, _w] = queue.pop()

                    for dx, dy in dir:
                        if _w + dx < 0 or _w + dx >= Width or _h + dy < 0 or _h + dy >= Height:
                            continue
                        if graph[_h + dy][_w + dx] == 1:
                            graph[_h + dy][_w + dx] = 0
                            queue.append([_h + dy, _w + dx])

    print(island)
