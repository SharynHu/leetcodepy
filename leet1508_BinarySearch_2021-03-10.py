class Solution(object):
    def countAndSum(self, nums, candidate):
        """
        this function returns how many subarrays in nums have sums less than or equal to candidate and the total sum of them.
        """
        count, curr, currSum, totalSum = [0]*4
        # maintain a window nums[i:j+1] where sum(nums[i:j+1])<=candidate.
        i = 0
        for j in range(len(nums)):
            # extend the window by 1
            curr += nums[j]
            currSum += nums[j]*(j-i+1)
            while(curr>candidate):
                currSum -= curr
                curr -= nums[i]
                i += 1
            # update count 
            count += j-i+1
            totalSum += currSum
        return [count, totalSum]
    
    def sumOfKSmallest(self, nums, k):
        left = min(nums)
        right = sum(nums)
        while(left+1<right):
            middle = (left+right)/2
            count, totalSum = self.countAndSum(nums, middle)
            # print middle, count, totalSum
            if count>=k:
                right = middle
            else:
                left = middle
        count, totalSum = self.countAndSum(nums, left)
        if count>=k:
            res = left
        else:
            res = right
        count, totalSum = self.countAndSum(nums, res)
        # there maybe duplicates in the 
        # print res, count, totalSum
        return totalSum-res*(count-k)
        
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        return (self.sumOfKSmallest(nums, right)-self.sumOfKSmallest(nums, left-1))%(10**9+7)
