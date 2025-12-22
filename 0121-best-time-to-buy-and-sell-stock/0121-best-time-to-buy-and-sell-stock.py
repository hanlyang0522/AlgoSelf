class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0] * len(prices)

        max_p = 0

        for idx in range(len(prices) - 1, -1, -1):
            max_p = max(max_p, prices[idx])
            profit[idx] = max_p - prices[idx]

        return max(profit)