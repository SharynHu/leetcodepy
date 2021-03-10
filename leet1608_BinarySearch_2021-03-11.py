# the bigger x is, there are less numbers greater than x in nums.
# so this is a binary search problem
class Solution(object):
    def count(self, nums, x):
        new_nums = [num for num in nums if num>=x]
        return len(new_nums)
    
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = max(nums)
        while(left+1<right):
            middle = (left+right)/2
            count = self.count(nums, middle)
            if count == middle:
                return middle
            if count<middle:
                right = middle
            else:
                left = middle
        # print left, right
        if self.count(nums, left)==left:
            return left
        if self.count(nums, right)==right:
            return right
        return -1
