class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        num = 0
        for i in range(len(s)):
            if i+1<len(s) and mapping[s[i+1]]>mapping[s[i]]:
                num -= mapping[s[i]]
            else:
                num += mapping[s[i]]
        return num
