class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        for can in candidates:
            dq = deque()
            dq.append([can])

            while dq:
                curr = dq.popleft()

                if sum(curr) > target or len(curr) > 150:
                    continue

                if sum(curr) == target:
                    if sorted(curr) not in ans:
                        ans.append(sorted(curr))
                    continue

                for ca in candidates:
                    dq.append(curr + [ca])

        return list(ans)