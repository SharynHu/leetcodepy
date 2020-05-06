# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s:
            return False
        if not t:
            return False
        if s.val!=t.val:
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isSameTree(s, t):
            return True
        if not s:
            return not t
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
