#由于正负号不确定，所以同时保留最大最小值
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        res = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        
        for i in range(1, len(nums)):
            currMax, currMin = max([currMax*nums[i], currMin*nums[i], nums[i]]), min([currMax*nums[i], currMin*nums[i], nums[i]])
            res = max(res,currMax)
        return res
