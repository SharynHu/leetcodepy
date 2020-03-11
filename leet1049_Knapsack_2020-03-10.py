class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        sum_ = sum(stones)
        dp = [False]*(sum_/2+1)
        dp[0] = True
       
        for i in range(len(stones)):
            for j in range(sum_/2, stones[i]-1, -1):
                dp[j] |= dp[j-stones[i]]
            
        for j in range(sum_/2, -1, -1):
            if dp[j]:
                return sum_-2*j
        return sum_
