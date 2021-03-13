# We know that the maximum average value must be between the minimal value (left in the code ) and maximum value (right in the code ) in nums. Each time we can check if mid = (left+right)/2 is larger or less than the the maximum average value:
# we use max_ave to denote the maximum average value. Then, for any i, j (j-i>=k-1), we can have (nums[i] - max_ave) + (nums[i+1] - max_ave)+...+ (nums[j] - max_ave) <=0. Therefore, for some i, j (j-i>=k-1), if we find (nums[i] - mid) + (nums[i+1] - mid)+...+ (nums[j] - mid) >0, then mid must be smaller than max_ave. 
# (cited from https://leetcode.com/problems/maximum-average-subarray-ii/discuss/105477/c-clean-binary-search-solution-with-explanation)


class Solution(object):
    def isSmaller(self, nums, middle, k):
        # suppose newNums = [x-middle for x in nums]
        # if the current value is bigger than the maximum average, then for any subarray of newNums with minimum length of k, of which the sum must be smaller than 0.
        # if the current value is smaller than the maximum average, then we can find at least one subarray of newNums with minimum length of k, of which the sum is bigger than 0.
        # As we can see the second situation is just the opposite of the first situation, so for simplisity we can just check the second situation. 
        currSum, prevSum, minSum = 0, 0, float('inf')
        # we need to record the minimum sum of nums[:i-k]
        for i in range(len(nums)):
            currSum += nums[i]-middle
            if i>=k:
                prevSum += nums[i-k]-middle
                minSum = min(prevSum, minSum)
            if (i>=k and currSum-minSum>0):
                return True
            if i>=k-1 and currSum>0:
                return True
        return False
    
    
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        left, right = min(nums), max(nums)
        
        while(left+10**(-5)<right):
            middle = (left+right)/2.0
            res = self.isSmaller(nums, middle, k)
            if res:
                # it means middle is too small
                left = middle
            else:
                right = middle
        print left, right
        # check left and right
        # check the smaller one if it is small
        if not self.isSmaller(nums, left, k):
            return left
        return right
