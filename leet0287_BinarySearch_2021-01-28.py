class Solution(object):
    def count(self, nums, k):
        count1, count2 = 0,0
        for num in nums:
            if num==k:
                count1 += 1
            if num<k:
                count2 += 1
        return count1, count2
    
    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right =len(nums)
        
        while(left+1<right):
            middle = (left+right)/2
            count1, count2 = self.count(nums, middle)
            if count1>1:
                return middle
            if count2<=middle-1:
                # this means the duplicated number is in range[middle, right]
                left = middle
            else:
                right = middle
        #check left, right
        if self.count(nums, left)[0]>1:
            return left     
        return right
