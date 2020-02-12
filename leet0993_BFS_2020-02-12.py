# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return False
        
        queue = deque()
        if root.left:
            queue.appendleft((root.left, root))
        if root.right:
            queue.appendleft((root.right, root))
        while(queue):
            size = len(queue)
            xParent = None
            yParent = None
            for i in range(size):
                curr, parent = queue.pop()
                if curr.val == x:
                    xParent = parent
                if curr.val == y:
                    yParent = parent
                if curr.left:
                    queue.appendleft((curr.left, curr))
                if curr.right:
                    queue.appendleft((curr.right, curr))
            if xParent and yParent and xParent!=yParent:
                return True
        return False