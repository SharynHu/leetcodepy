class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for char in S:
            if char == "(":
                stack.append(char)
                continue
            if char == ")":
                scores = []
                while(stack and stack[-1]!="("):
                    scores.append(stack.pop())
                stack.pop()
                if not scores:
                    stack.append(1)
                else:
                    stack.append(2*sum(scores))
        return sum(stack)
