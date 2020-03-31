# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#使用栈实现中序遍历
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """ 
        self.stack = []
        if root:
            self.stack.append(root)
        while(self.stack and self.stack[-1].left):
            self.stack.append(self.stack[-1].left)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        #要想访问栈顶元素，必须保证当前栈顶元素的左子树已经全部被访问完毕
        currNode = self.stack.pop()
        x = currNode.val
        if not currNode.right:
            return x
        self.stack.append(currNode.right)
        while(self.stack[-1].left):
            self.stack.append(self.stack[-1].left)
        return x

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.stack:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
