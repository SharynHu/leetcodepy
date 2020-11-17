class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j= 0, len(nums)-1
        while(i<j):
            if nums[i]+nums[j] == target:
                return [i+1, j+1]
            if nums[i]+nums[j] < target:
                i += 1
            else:
                j -= 1
