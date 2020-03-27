#find the common subsequece of s1 and s2 which has the smallest ASCII sum
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)
        
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+(ord(s1[i-1])*(s1[i-1]==s2[j-1]) ))
        return sum(map(ord, s1+s2))-dp[-1][-1]*2
