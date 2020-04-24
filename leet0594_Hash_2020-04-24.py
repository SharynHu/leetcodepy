class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        
        maxLen = 0 
        for minimum in counter:
            if minimum+1 not in counter:
                continue
            maxLen = max(maxLen, counter[minimum]+counter[minimum+1])
        return maxLen
            
