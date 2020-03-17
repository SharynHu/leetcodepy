class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_%2 !=0:
            return False
        
        dp = set([0])
        for num in nums:
            dp |= set([i+num for i in dp])
        
        return sum_/2 in dp
