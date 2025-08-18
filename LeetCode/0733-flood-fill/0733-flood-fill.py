from collections import deque


dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        targetC = image[sr][sc]
        m, n = len(image), len(image[0])
        image[sr][sc] = color

        li = deque()
        li.append([sr, sc])

        while li:
            ty, tx = li.popleft()

            for dy, dx in dirs:
                tty, ttx = ty + dy, tx + dx

                if tty < 0 or tty >= m or ttx < 0 or ttx >= n:
                    continue

                if image[tty][ttx] == targetC:
                    image[tty][ttx] = color
                    li.append([tty, ttx])

        return image