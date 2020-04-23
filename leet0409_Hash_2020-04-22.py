class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        
        res = 0
        flag = False
        for char in count:
            res += (count[char]/2)*2
            if not flag and count[char]%2==1:
                flag = True
            
        return res+flag
