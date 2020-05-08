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
        #将左子树全部入栈，确保栈顶元素是最小的元素
        while(self.stack and self.stack[-1].left):
            self.stack.append(self.stack[-1].left)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        #现在栈顶元素是最小的元素，也就是说它的左子树已经全部访问完了
        #访问栈顶元素
        currNode = self.stack.pop()
        currVal  = currNode.val
        #如果栈顶元素有右子树，应该将其右子树及其右子树的左子树入栈
        if currNode.right:
            self.stack.append(currNode.right)
            while(self.stack and self.stack[-1].left):
                self.stack.append(self.stack[-1].left)
        return currVal

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.stack:
            return False
        return True
