class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        i,j=0,1
        while(i<len(nums) and j<len(nums)):
            # make sure that i is the first nums[i]
            if i-1>=0 and nums[i-1]==nums[i]:
                i += 1
                continue
            if j<=i:
                j = i+1
                continue
            if nums[j]-nums[i]==k:
                count += 1
                i += 1
                continue
            if nums[j]-nums[i]<k:
                j += 1
                continue
            if nums[j]-nums[i]>k:
                i += 1
                continue
        return count
                
        
        
