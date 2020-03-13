class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:
            return 1
        
        dp = [[0]*(n+1) for i in range(m+1)]
        #Initialization of the dp array
        for i in range(1, m+1):
            dp[i][1] = 1
        for j in range(1, n+1):
            dp[1][j] = 1
         
        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
