class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            currStart, currEnd = interval
            prevStart, prevEnd = res[-1]
            if currStart<=prevEnd:
                res[-1][1] = max(prevEnd, currEnd)
            else:
                res.append(interval)
        return res
