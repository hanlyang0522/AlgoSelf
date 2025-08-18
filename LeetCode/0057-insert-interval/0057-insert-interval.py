class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        n = len(intervals)
        li = []
        i = 0

        # 겹치기 전까지는 그대로 추가
        while i < n and intervals[i][1] < newInterval[0]:
            li += [intervals[i]]
            i += 1

        # 겹친 후에는 안 겹치는거 나올 때까지 업데이트
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # 끝났으면 니머지 그대로 추가
        li += [newInterval]
        li += intervals[i::]

        return li