class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        maxLen  = 0
        for char in s:
            if char=='(':
                left += 1
            if char==')':
                right += 1
            if left==right:
                maxLen = max(maxLen, left)
            if right>left:
                left, right = 0, 0
                
        left, right = 0, 0
        for char in s[::-1]:
            if char==')':
                right += 1
            if char=='(':
                left += 1
            if left==right:
                maxLen = max(maxLen, left)
            if left>right:
                left, right = 0, 0
        return maxLen*2
