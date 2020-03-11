#解法二，将此问题转换为有两个限制条件的0-1背包问题
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for string in strs:
            numOfOnes = sum(map(int, list(string)))
            numOfZeros = len(string)-numOfOnes
            for i in range(m, numOfZeros-1, -1):
                for j in range(n, numOfOnes-1, -1):
                    dp[i][j] = max([dp[i][j],  dp[i-numOfZeros][j-numOfOnes]+1])

        return dp[-1][-1]
