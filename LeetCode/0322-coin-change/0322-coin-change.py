class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for w in range(1, amount + 1):
            for i in range(n):
                if coins[i] <= w:
                    dp[w] = min(dp[w], dp[w - coins[i]] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1