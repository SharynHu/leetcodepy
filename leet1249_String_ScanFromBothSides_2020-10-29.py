class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #first remove from left to right
        left, right = 0,0
        validStrLeft = ""
        for char in s:
            if char.isalpha():
                validStrLeft += char
                continue
            if char == "(":
                left += 1
                validStrLeft += char
                continue
            if char==")":
                if right<left:
                    # we can keep this ")"
                    right += 1
                    validStrLeft += char
            # else we discard this ")" and do nothing
        print validStrLeft
        #remove from right to left
        left, right = 0,0
        validStrRight = ""
        for i in range(len(validStrLeft)-1, -1, -1):
            char = validStrLeft[i]
            if char.isalpha():
                validStrRight = char +validStrRight
            if char == ")":
                right += 1
                validStrRight = char+validStrRight
                continue
            if char=="(":
                if left<right:
                    # we can keep this "("
                    left += 1
                    validStrRight = char+validStrRight
            # else we discard this "(" and do nothing   
        return validStrRight
                    
           
