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
        if not root:
            return 0
        currLen = 1
        leftLen = self.dfs(root.left)
        rightLen = self.dfs(root.right)
        if root.left and root.val == root.left.val-1:
            currLen = leftLen+1
        if root.right and root.val == root.right.val-1:
            currLen  = max(currLen, rightLen+1)
        self.maxLen = max(self.maxLen, currLen)
        return currLen
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.maxLen
