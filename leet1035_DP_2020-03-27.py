class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max([dp[i][j-1], dp[i-1][j], dp[i-1][j-1]+int(A[i-1]==B[j-1])])
        
        return dp[-1][-1]
