class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        valid = set(map(str, range(1, 27)))
        if s[0] != "0":
            dp[1] = 1
        for i in range(1, len(s)):
            if s[i] not in valid and s[i-1:i+1] not in valid:
                dp[i+1] = 0
                continue
            if dp[i]==0 and dp[i-1] == 0:
                dp[i+1] = 0
                continue
            if s[i] in valid:
                dp[i+1] += dp[i]
            if s[i-1:i+1] in valid:
                dp[i+1] += dp[i-1]
        return dp[-1]
        
