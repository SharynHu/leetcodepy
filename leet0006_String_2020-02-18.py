#Solution:
#1. if numRows==1:return s
#2. if numRows==2:return s[::2]+s[1::2]
#3. if numRows>=3:
#   we devide string s into groups of size 2*numRows-1; 
    
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # corner cases
        if numRows==1:
            return s
        if numRows==2:
            return s[::2]+s[1::2]
        
        # numRows>=3
        res = [""]*numRows
        groupSize = 2*numRows-2
        
        # for each letter we find its position in each group
        for i in range(len(s)):
            groupIndex = (i+1)%groupSize
            if groupIndex == 0:
                groupIndex = groupSize
            if groupIndex<=numRows:
                res[groupIndex-1] += s[i]
                continue
            groupIndex -= numRows
            res[-groupIndex-1] += s[i]
        # print res
        return "".join(res)
