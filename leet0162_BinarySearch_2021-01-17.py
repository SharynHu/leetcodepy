# There must be a peak in the array and
# nums[i]!=nums[i+1]
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        
        nums=[float('-inf')]+nums+[float('-inf')]
        # now there are at least 3 numbers in te array.
        left, right = 1, len(nums)-2
        while(left+1<right):
            middle = (left+right)/2
            # if we are lucky enough, we can find a peak right at middle.
            if nums[middle]>nums[middle-1] and nums[middle]>nums[middle+1]:
                return middle-1
            # or else nums[middle-1:middle+2] is sorted, either in descending order or in ascending order.
            # if it is in descending order:
            if nums[middle]>nums[middle+1]:
                # nums[start], nums[middle], nums[middle+1] curves like low-high-low, so the peak must be between left and middle
                right = middle
            else:
                left = middle
        # check left and right
        if nums[left]>nums[left+1]:
            return left-1
        if nums[right-1]<nums[right]:
            return right-1
