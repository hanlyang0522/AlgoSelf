dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Solution:
    def dfs(self, grid, visit, y, x):
        m, n = len(grid), len(grid[0])

        dq = deque()
        dq.append([y, x, 0])

        while dq:
            cy, cx, ctime = dq.popleft()
            visit[cy][cx] = ctime

            for dy, dx in dirs:
                ty, tx = cy + dy, cx + dx

                if (
                    0 <= ty < m
                    and 0 <= tx < n
                    and grid[ty][tx] == 1
                    and ctime + 1 < visit[ty][tx]
                ):
                    dq.append([ty, tx, ctime + 1])

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        visit = [[float("inf")] * n for _ in range(m)]

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 2:
                    self.dfs(grid, visit, y, x)

        max_time = 0

        for y in range(m):
            if max_time == -1:
                break

            for x in range(n):
                if grid[y][x] == 1 and visit[y][x] == float("inf"):
                    max_time = -1
                    break
                elif visit[y][x] != float("inf"):
                    max_time = max(max_time, visit[y][x])

        return int(max_time)