class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        currSum  = 0
        maxSum = nums[0]
        
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            if currSum<0:
                currSum = 0
        return maxSum
            
