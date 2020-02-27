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
        for i in range(1, len(dp)):
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=-1:
                    dp[i] = min(dp[i], dp[i-coin]+1)
            if dp[i] == float('inf'):
                dp[i] = -1
        return dp[-1]
