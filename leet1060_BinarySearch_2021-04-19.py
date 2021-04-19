class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # corner cases that the k-th missing number is out of array as per this question on the right side of the array
        if nums[-1]-nums[0]-(len(nums)-1)<k:
            return k-(nums[-1]-nums[0]-(len(nums)-1))+nums[-1]
        
        left = 0
        right = len(nums)-1
        
        # keep the k-th missing number between left and right
        while(left+1<right):
            middle = (left+right)/2
            # so there are middle+1 numbers in nums[:middle+1], and there should be nums[middle]-nums[0]+1 numbers, so there are nums[middle]-nums[0]+1-middle numbera missing
            if nums[middle]-nums[0]-middle>=k:
                right = middle
            else:
                left = middle
        left_count =  nums[left]-nums[0]-left
        return nums[left]+k-left_count
