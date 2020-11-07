class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res
