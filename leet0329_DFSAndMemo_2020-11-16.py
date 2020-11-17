class Solution(object):
    def dfs(self, matrix, i, j, memo):
        if memo[i][j]!=0:
            return memo[i][j]
        for m, n in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if 0<=m<len(matrix) and 0<=n<len(matrix[0]) and matrix[m][n]>matrix[i][j]:
                memo[i][j] = max(memo[i][j], self.dfs(matrix, m, n, memo))
        memo[i][j] += 1
        return memo[i][j]
        
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # build graph
        memo = [[0]*len(matrix[0]) for i in range(len(matrix))]
        maxLen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxLen = max(maxLen, self.dfs(matrix, i, j, memo))
        return maxLen
