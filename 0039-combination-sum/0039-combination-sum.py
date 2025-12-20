class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        for i in range(len(candidates)):
            dq = deque()
            dq.append([[candidates[i]], i])

            while dq:
                curr, idx = dq.popleft()

                if sum(curr) > target or len(curr) > 150:
                    continue

                if sum(curr) == target:
                    if curr not in ans:
                        ans.append(curr)
                    continue

                for j in range(idx, len(candidates)):
                    dq.append([curr + [candidates[j]], j])

        return list(ans)