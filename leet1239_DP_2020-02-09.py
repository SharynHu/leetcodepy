#列举出所有可能选出最大的那个
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        if not arr:
            return 0
        
        
        dp = [set()]
        
        for word in arr:
            # if there are dupplicate letters in word, we skip it
            if len(word)>len(set(word)):
                continue
            word = set(word)
            size = len(dp)
            for i in range(size):
                if word&dp[i]:
                    continue
                dp.append(word|dp[i])
                
        return max([len(x) for x in dp])
        