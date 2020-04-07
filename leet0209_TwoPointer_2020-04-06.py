class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums)<s:
            return 0
    
        currSum = 0
        minLen = len(nums)
        i, j = 0, 0
        while(j<len(nums)):
            currSum += nums[j]
            
            while(i<=j and currSum>=s):
                #update minLen
                minLen = min(minLen, j-i+1)
                # check if we can find a smaller length
                currSum -= nums[i]
                i += 1
            j += 1
        return minLen
