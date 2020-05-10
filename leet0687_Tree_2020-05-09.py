# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxLen = 0
        
    def dfs(self, root):
        if  not root:
            return 0
        if not root.left and not root.right:
            self.maxLen = max(self.maxLen, 1)
            return 1
        currLen = 1
        leftLen = self.dfs(root.left)
        rightLen = self.dfs(root.right)
        if root.left and root.left.val==root.val:
            currLen +=  leftLen
        if root.right and root.right.val==root.val:
            currLen = max(currLen,rightLen+1)
        if root.left and root.right and root.left.val==root.right.val and root.val==root.left.val:
            self.maxLen = max(self.maxLen, leftLen+rightLen+1)
        self.maxLen = max(self.maxLen, currLen) 
        return currLen
        
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return max(self.maxLen-1, 0)
