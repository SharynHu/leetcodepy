class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left = 0
        right = len(nums)-1
        while(left+1<right):
            middle = (left+right)/2
            if nums[middle]==target:
                return True
            if nums[left]==nums[middle]:
                left += 1
                continue
            if nums[right] == nums[middle]:
                right -= 1
                continue
            #here nums[left]!=nums[middle] and nums[right]!=nums[middle]
            if nums[left]<=nums[middle]<target or target<nums[left]<nums[middle] or nums[middle]<target<=nums[right]:
                left = middle
            else:
                right = middle
        if nums[left] == target:
            return True
        if nums[right] == target:
            return True
        return False
