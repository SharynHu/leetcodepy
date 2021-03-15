class Solution(object):
    def findClosestElements(self, nums, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-k
        while(left+1<right):
            middle = (left+right)/2
            if nums[middle+k-1]<=x:
                left = middle
                continue
            if nums[middle]>=x:
                right = middle
                continue
            if nums[middle+k]-x<x-nums[middle]:
                left = middle
                continue
            right = middle
        if abs(nums[left]-x)<=abs(nums[right+k-1]-x):
            return nums[left:left+k]
        return nums[right:right+k]
            
