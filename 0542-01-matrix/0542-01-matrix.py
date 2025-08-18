class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dq = deque()

        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    dq.append([y, x])
                else:
                    mat[y][x] = -1

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while dq:
            y, x = dq.popleft()

            for dy, dx in dirs:
                ty, tx = y + dy, x + dx

                if 0 <= ty < m and 0 <= tx < n and mat[ty][tx] == -1:
                    mat[ty][tx] = mat[y][x] + 1
                    dq.append([ty, tx])

        return mat