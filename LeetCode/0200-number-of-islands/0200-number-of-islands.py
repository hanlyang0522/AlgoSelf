dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Solution:
    def dfs(self, grid, y, x):
        m, n = len(grid), len(grid[0])

        dq = deque()
        dq.append([y, x])
        grid[y][x] = 0

        while dq:
            cy, cx = dq.popleft()

            for dy, dx in dirs:
                ty, tx = cy + dy, cx + dx

                if 0 <= ty < m and 0 <= tx < n and grid[ty][tx] == "1":
                    dq.append([ty, tx])
                    grid[ty][tx] = "0"

        return 1

    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        n_island = 0

        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    n_island += 1
                    self.dfs(grid, y, x)

        return n_island
