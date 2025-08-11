class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = prices[0]
        profit = 0

        for i in prices[1:]:
            best_price = min(best_price, i)
            profit = max(profit, i - best_price)

        return profit