class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #dp[i] means s[:i] is breakable
        dp = [False]*(len(s)+1)
        #Initialization
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for word in wordDict:
                dp[i] |= (i-len(word)>=0 and dp[i-len(word)] and s[i-len(word):i]==word)
        
        
        return dp[len(s)]
                    
