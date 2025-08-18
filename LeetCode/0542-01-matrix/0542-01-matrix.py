from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        visited = [[float("inf")] * n for _ in range(m)]

        dq = deque()

        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    dq.append([y, x, 0])
                    visited[y][x] = 0

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while dq:
            y, x, depth = dq.popleft()

            if visited[y][x] < depth:
                continue

            visited[y][x] = depth

            for dy, dx in dirs:
                ty, tx = y + dy, x + dx

                if 0 <= ty < m and 0 <= tx < n and visited[ty][tx] > depth + 1:
                    dq.append([ty, tx, depth + 1])

        return visited