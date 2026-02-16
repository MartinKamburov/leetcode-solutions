class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Using a bottom up approach we can take the minimum number of ways to get the final amount 
        # one by one slowly growing and using memoization at each step
        for a in range(1, amount + 1):
            # we loop through each coin and check if the difference between the index and coin is greater than 0
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1