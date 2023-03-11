"""
edge의 가중치가 모두 동일 --> BFS로 최단거리 구할 수 있음!
"""


from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(start, maps):
    queue = deque()

    y, x, cnt = start
    maps[y][x] = cnt
    queue.append((y, x, cnt))

    while queue:
        y, x, cnt = queue.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if ny == len(maps) - 1 and nx == len(maps[0]) - 1:
                return cnt + 1
            elif 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                queue.append((ny, nx, cnt + 1))
    return -1


def solution(maps):
    return bfs((0, 0, 1), maps)
