class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        if amount == 0:
            return amount
        for coin in coins:
            if coin == amount:
                return 1

        max_value = 2**31-1
        dp = [max_value]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)

        print(dp)
        if dp[amount] == max_value:
            return -1
        return dp[amount]