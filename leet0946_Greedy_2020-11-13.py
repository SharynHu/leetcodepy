class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        
        while(pushed or popped):
            # when to push
            if pushed:
                if not stack or not popped or popped[0]!=stack[-1]:
                    stack.append(pushed.pop(0))
                    continue
            #when to pop
            if popped:
                if stack and stack[-1]==popped[0]:
                    popped.pop(0)
                    stack.pop()
                    continue
            return False
        return True
