class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        if k == 1:
            return ""
        for char in s:
            if not stack or stack[-1][0]!=char:
                stack.append([char, 1])
                continue
            #when we put a new char into the stack, we compare it with the last char
            #if they are equal, we increase the count of the char
            if char==stack[-1][0]:
                stack[-1][1] += 1
                #check if we can delete the char
                if stack[-1][1]==k:
                    stack.pop()
                continue
        res = ""
        for char, count in stack:
            res += char*count
        return res

                
