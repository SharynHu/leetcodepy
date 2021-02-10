class Solution(object):
    def check(self, nums, divisor):
        res = 0
        for num in nums:
            res += num/divisor
            if num%divisor>0:
                res += 1
        return res
    
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right = sum(nums)
        
        while(left+1<right):
            middle = (left+right)/2
            currRes = self.check(nums, middle)
            if currRes>threshold:
                left = middle
            else:
                right = middle
        # check left
        if self.check(nums, left)<=threshold:
            return left
        return right
