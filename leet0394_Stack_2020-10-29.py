class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currString = ""
        count = ""
        for char in s:
            if char.isdigit():
                count += char
                if currString:
                    stack.append(currString)
                    currString = ""
                    continue
            if char.isalpha():
                currString += char
                continue
            if char == "[":
                if not count:
                    stack.append(1)
                else:
                    stack.append(int(count))
                stack.append("[")
                count = ""
                continue
            if char == "]":
                combinedStr = currString
                while(stack and stack[-1]!="["):
                    combinedStr = stack.pop()+combinedStr
                stack.pop()
                stack.append(stack.pop()*combinedStr)
                currString = ""
        if currString:
            stack.append(currString)
        return "".join(stack)
