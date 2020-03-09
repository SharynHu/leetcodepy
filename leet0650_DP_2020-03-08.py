class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        #对于每个n,最多需要n次， 一次copy和n-1次paste
        dp = range(n+1)
        dp[0] =0
        dp[1] = 0
        dp[2] = 2
        for i in range(2, n+1):
            for j in range(1, i):
                if i%j==0:
                    dp[i] = min(dp[i], (i/j-1)+dp[j]+1)
        return dp[n]
