#Approach:
# 1. flip the whole string
# 2. flip each word in the string

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #first reverse s
        for i in range(len(s)/2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        print s
        
        #reverse  each word
        start = 0
        end = 0
        while(start<len(s) and end<=len(s)):
            # let end points to the end or the space
            while(end<len(s) and s[end]!=' '):
                end += 1
            # now s[end]==" " or end is at the end of s, we need to flip s[start:end]
            for i in range(start, start+(end-start)/2):
                s[i], s[start+end-i-1] = s[start+end-i-1], s[i]
            end += 1
            start = end
