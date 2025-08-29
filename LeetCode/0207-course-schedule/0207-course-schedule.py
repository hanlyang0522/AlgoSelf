class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parent = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for x, y in prerequisites:
            parent[y].append(x)
            inDegree[x] += 1

        dq = deque([i for i in range(numCourses) if inDegree[i] == 0])
        noPre = [False] * numCourses

        while dq:
            x = dq.pop()
            noPre[x] = True

            for p in parent[x]:
                inDegree[p] -= 1

                if inDegree[p] == 0:
                    dq.append(p)

        print(noPre)

        return False not in noPre