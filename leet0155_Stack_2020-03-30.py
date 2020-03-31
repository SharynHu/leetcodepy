class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.number = []
        self.minimum = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.number.append(x)
        if not self.minimum:
            self.minimum.append(x)
            return
        if x<= self.minimum[-1]:
            self.minimum.append(x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.number.pop()
        if x<=self.minimum[-1]:
            self.minimum.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.number[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
