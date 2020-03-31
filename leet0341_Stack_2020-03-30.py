#使用hasNext展开栈顶的nestedInteger, 确保栈顶都是整型数据
#next用来获取栈顶元素

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()
        
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return False
        top = self.stack.pop()
        if top.isInteger():
            self.stack.append(top)
            return True
        topList = top.getList()
        self.stack += topList[::-1]
        return self.hasNext()
        


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
