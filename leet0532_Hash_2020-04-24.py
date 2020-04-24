class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = collections.Counter(nums)
        if k<0:
            return 0
        
        res = 0
        for val in counter:
            if k == 0:
                if counter[val] >=2:
                    res += 1
                continue
            if counter[val+k]:
                res += 1
        return res
