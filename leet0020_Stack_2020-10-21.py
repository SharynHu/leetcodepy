class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if char in ")]}":
                if stack[-1]!=pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
        
