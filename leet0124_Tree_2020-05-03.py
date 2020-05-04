# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxSum = float('-inf')
        
    def dfs(self, root):
        if not root:
            return 0
        leftSum = self.dfs(root.left)
        rightSum = self.dfs(root.right)
        currSum = max([leftSum, rightSum, 0, leftSum+rightSum])+root.val
        self.maxSum = max(self.maxSum, currSum)
        return max([leftSum, rightSum, 0])+root.val
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root)
        return self.maxSum
        
