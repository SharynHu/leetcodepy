#不用去重
#使用hash set
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToIndex = {}
        
        for i in range(len(nums)):
            if target-nums[i] in numToIndex:
                return [i, numToIndex[target-nums[i]]]
            numToIndex[nums[i]] = i
        
