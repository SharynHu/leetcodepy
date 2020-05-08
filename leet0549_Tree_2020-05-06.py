# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxLen = 0
        
        
    def maxPath(self, root):
        if not root:
            return 0, 0
        currInc, currDec = 1, 1
        leftInc, leftDec = self.maxPath(root.left)
        rightInc, rightDec = self.maxPath(root.right)
        if root.left:
            if root.left.val == root.val-1:
                currInc = leftInc +1
            if root.left.val == root.val+1:
                currDec = leftDec+1
        if root.right:
            if root.right.val == root.val-1:
                currInc = max(currInc, rightInc+1)
            if root.right.val == root.val+1:
                currDec = max(currDec, rightDec+1)
        self.maxLen = max(currInc+currDec-1, self.maxLen)
        return currInc, currDec
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath(root)
        return self.maxLen
