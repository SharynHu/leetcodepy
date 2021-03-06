class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        
        maxSize = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "0":
                    dp[i][j] = 0
                    continue
                dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]])+1
                maxSize = max(maxSize, dp[i][j])
        return maxSize**2
