class Solution(object):
    def countNum(self, nums, m, candidate):
        count, currSum = 1, 0 
        for num in nums:
            currSum += num
            if currSum>candidate:
                currSum  = num # Start new container
                count  += 1
        return count
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # we know that the answer must lie between max(nums) and sum(nums)
        left = max(nums)
        right = sum(nums)
        
        while(left+1<right):
            middle = (left+right)/2
            # if the largest subarray sum is middle, we calculate how many groups we need to devide nums into such that the largest subarray sum is less than or equal to middle
            count = self.countNum(nums, m, middle)
            if count<=m:
                right = middle
            else:
                left = middle
        # check left
        count = self.countNum(nums, m,left)
        if count<=m:
            return left
        return right
