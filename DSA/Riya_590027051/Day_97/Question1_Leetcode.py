class Solution:
    def coinChange(self, coins, amount):
        # dp[i] = minimum number of coins needed to make amount i
        dp = [amount + 1] * (amount + 1)

        # 0 coins are needed to make amount 0
        dp[0] = 0

        # Calculate answer for every amount from 1 to amount
        for i in range(1, amount + 1):

            for coin in coins:

                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If amount is still impossible
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]