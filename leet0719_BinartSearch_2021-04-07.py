class Solution(object):  
    def count(self, nums, candidate):
        '''
        count how many pairs has distance less than or equal to candidate
        '''
        j = 0
        count = 0
        for i in range(len(nums)):
            while(nums[i]-nums[j]>candidate):
                j += 1
            count += i-j
        return count
            
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = nums[-1]-nums[0]
        
        while(left+1<right):
            middle = (left+right)/2
            if self.count(nums,middle)>=k:
                right = middle
            else:
                left = middle
        if self.count(nums,left)>=k:
            return left
        return right
