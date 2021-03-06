class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        if len(nums)==1:
            return nums[0]
        
        minimum = float('inf')
        left, right = 0, len(nums)-1
        
        while(left+1<right):
            minimum = min([nums[left], nums[right], minimum])
            middle = (left+right)/2
            if nums[middle]==nums[left]:
                left += 1
                continue
            if nums[right]==nums[middle]:
                right -= 1
                continue
            if nums[middle]>nums[left]:
                left = middle
                continue
            if nums[middle]<nums[right]:
                right = middle
        minimum = min([nums[left], nums[right], minimum])
        return minimum
