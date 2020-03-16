class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #dp[i] denotes the minimum number of coins needed for amount i
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                if dp[j-coin] != float('inf'):
                    dp[j] = min(dp[j], dp[j-coin]+1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
        
