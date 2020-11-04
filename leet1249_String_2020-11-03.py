class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        right = 0
        for char in s:
            if char==")":
                right += 1
        
        validStr = ""
        left = 0
        for char in s:
            if char not in "()":
                validStr += char 
                continue
            if char == "(":
                #查看右侧是否有")"与其匹配
                if right>0:
                    right -= 1
                    validStr += "("
                    left += 1
            if char == ")":
                if left>0:
                    left -= 1
                    validStr += ")"
                else:
                    right -= 1
        return validStr
