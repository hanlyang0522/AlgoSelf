class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li = []

        for p in points:
            dist = p[0] ** 2 + p[1] ** 2
            li.append([p, dist])

        li = sorted(li, key=lambda x: x[1])
        topK = li[:k]

        return [list(x[0]) for x in topK]