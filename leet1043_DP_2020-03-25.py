# dp[i] record the maximum sum we can get considering A[0] ~ A[i]
# To get dp[i], we will try to change k last numbers separately to the maximum of them,
# where k = 1 to k = K.
class Solution(object):       
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A)<=K:
            return len(A)*max(A)
        
        dp = [0]*(len(A)+1)
      
        for i in range(1, len(A)+1):
            for k in range(1, min(i+1, K+1)):
                maximum = max(A[i-k:i])*k
                dp[i] = max(dp[i], dp[i-k]+maximum)
        return dp[-1]
        
