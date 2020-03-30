class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 0
            count[i] += 1
            
        res = -1
        for k in count:
            if k==count[k]:
                res = max(res, k)
        return res
