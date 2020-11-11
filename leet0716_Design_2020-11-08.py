class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.max = []
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if not self.max:
            self.max.append(x)
        else:
            self.max.append(max(x, self.max[-1]))

    def pop(self):
        """
        :rtype: int
        """
        self.max.pop()
        return self.data.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max[-1]
        

    def popMax(self):
        """
        :rtype: int
        """
        tmp = []
        while(self.data and self.data[-1]!=self.max[-1]):
            tmp.append(self.data.pop())
            self.max.pop()
        x = self.data.pop()
        self.max.pop()
        while(tmp):
            self.data.append(tmp.pop())
            if not self.max:
                self.max.append(self.data[-1])
            else:
                self.max.append(max(self.data[-1], self.max[-1]))
        return x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
