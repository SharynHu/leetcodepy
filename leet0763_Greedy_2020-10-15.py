#variant of merge intervals
class Solution(object):
    def partitionLabels(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        lastIndex = {}
        res = []
        
        # get the last position for each charactor
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        # then loop through the string s
        for i in range(len(s)):
            startIndex = i
            endIndex = lastIndex[s[i]]
            if not res:
                res.append([startIndex, endIndex])
                continue
            prevStart, prevEnd = res[-1]
            if startIndex>prevEnd:
                res.append([startIndex, endIndex])
                continue
            if startIndex<=prevEnd:
                res[-1][-1] = max(prevEnd, endIndex)
                continue
        return [end-start+1 for start,end in res]
