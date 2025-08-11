class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dpMin = [10**5] * len(prices)
        dpMax = [0] * len(prices)

        minV = 10**5
        maxV = 0

        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > maxV:
                maxV = prices[i]
            dpMax[i] = maxV

        for i in range(len(prices)):
            if prices[i] < minV:
                minV = prices[i]
            dpMin[i] = minV

        diff = 0
        for i, j in zip(dpMin, dpMax):
            if j - i > diff:
                diff = j - i

        return diff
