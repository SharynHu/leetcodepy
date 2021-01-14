class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return False
        left, right = 0, len(nums)-1
        
        while(left+1<right):
            middle = (left+right)/2
            if nums[middle] == target:
                return True
            if nums[left]==nums[middle]:
                left += 1
                continue
            if nums[right]==nums[middle]:
                right -= 1
                continue
            # if the left part is sorted
            if nums[left]<nums[middle]:
                if nums[left]<=target<nums[middle]:
                    right = middle
                else:
                    left = middle
            # if the right side is sorted
            else:
                if nums[middle]<nums[right]:
                    left = middle
                else:
                    right = middle              

        if nums[left]==target:
            return True
        if nums[right]==target:
            return True
        return False
