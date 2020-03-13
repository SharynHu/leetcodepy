# 对于任意的一个字符串s, 
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            if s[0] == '0':
                return 0 
            return 1
        
        valid = set(map(str, range(1, 27)))
        #Initialization of the dp array
        prev0 = 1
        if  s[0] in valid:
            prev1 = 1
 
            
        for i in range(2, len(s)+1):
            #count counts how many in s[i-1]+s[i] and s[i] are valid
            if s[i-1] not in valid and s[i-2]+s[i-1] not in valid:
                dp[i] = 0
                continue
            if s[i-1] in valid and s[i-2]+s[i-1] in valid:
                dp[i] = dp[i-2]+dp[i-1]
                continue
            if s[i-1] in valid:
                dp[i] = dp[i-1]
                continue
            if s[i-2]+s[i-1] in valid:
                dp[i] = dp[i-2]
        return dp[-1]
