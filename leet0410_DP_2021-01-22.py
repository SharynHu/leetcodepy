class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # corner cases
        if m==1:
            return sum(nums)
        
        # dp[i][j] means the largest subarray sum splitting subarray nums[:j+1] into i parts. 
        dp = [[float('inf')]*len(nums) for i in range(m+1)]
        
        preSum = [0]
        for j in range(len(nums)):
            preSum.append(preSum[-1]+nums[j])
            
        #Initialize dp
        for j in range(len(nums)):
            dp[1][j] = preSum[j+1]
        
        for i in range(2, m+1):
            for j in range(len(nums)):
                for k in range(i-1,j+1):
                    # we try to split nums[:k] into i-1 subarrays and nums[k:] is the remaining subaray
                    # print i, j, k, dp[i-1][k], preSum[len(nums)]-preSum[k+1]
                    dp[i][j] = min(dp[i][j], max(dp[i-1][k-1], preSum[j+1]-preSum[k]))
        return dp[-1][-1]
                    
        
        
        
