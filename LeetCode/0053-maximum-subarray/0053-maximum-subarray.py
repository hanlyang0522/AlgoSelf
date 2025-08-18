class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_profit = 0
        max_profit = -(10**4)

        for n in nums:
            curr_profit += n

            if n > curr_profit:
                curr_profit = n

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit