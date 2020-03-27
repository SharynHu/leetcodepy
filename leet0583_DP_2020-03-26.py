#寻找两个字符串的最长公共子序列
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        #dp[i][j] means the length of the longest common subsequence of word1[:i] and word2[:j]
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+(word1[i-1] == word2[j-1]))
        return m+n-dp[-1][-1]*2
