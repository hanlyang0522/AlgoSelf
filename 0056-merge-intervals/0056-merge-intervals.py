class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for inter in intervals[1:]:
            if prev[1] >= inter[0]:  # overlapped
                prev[1] = max(prev[1], inter[1])
            else:
                ans.append(prev)
                prev = inter

        ans.append(prev)

        return ans