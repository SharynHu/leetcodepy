class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = range(n+1)
        for i in range(2, n+1):
            for j in range(1, int(n**0.5)+1):
                dp[i] = min(dp[i], dp[i-j**2]+1)
        return dp[n]
