class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = defaultdict(int)
        length = len(nums)
        ans = -1
        for n in nums:
            di[n] += 1

            if di[n] >= length / 2:
                ans = n
                break

        return ans