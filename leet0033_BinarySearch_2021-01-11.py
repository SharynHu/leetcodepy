# The key point is to decide which side target is on, on the left side of nums middle or on the right side of nums[middle]. 
# If the array is sorted, then it would be quite easy, we just need to compare target and nums[middle].
# But now maybe only part of the array is sorted, whcih menas the obove  startergy does not work any more.
# So here is the observation:
#    if nums[middle]>nums[left], then nums[left:middle+1] is sorted; if nums[middle]<nums[right], then nums[middle:right+1] is sorted.
# To decide which part we need to reserve, we just need to tell whether target is in the "sorted" part or not, which is far more easier.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while(left+1<right):
            # print left, right
            middle = (left+right)/2
            if nums[middle] == target:
                return middle
            # if the left part is sorted
            if nums[left]<nums[middle]:
                if nums[left]<=target<nums[middle]:
                    right = middle
                else:
                    left = middle
            # if the right part is sorted
            else:
                if nums[middle]<target<=nums[right]:
                    left = middle
                else:
                    right = middle
                    
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        return -1
