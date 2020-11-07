class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.tmp = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        for i in range(len(self.data)-1):
            self.tmp.append(self.data.pop())
        x = self.data.pop()
        for i in range(len(self.tmp)):
            self.data.append(self.tmp.pop())
        return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        for i in range(len(self.data)):
            self.tmp.append(self.data.pop())
        x = self.tmp[-1]
        for i in range(len(self.tmp)):
            self.data.append(self.tmp.pop())
        return x

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.data)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
