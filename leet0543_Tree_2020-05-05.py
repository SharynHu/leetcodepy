# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxLen = 0
        
    def pathLen(self, root):
        if not root:
            return 0
        leftLen = self.pathLen(root.left)
        rightLen = self.pathLen(root.right)
        self.maxLen = max(self.maxLen, leftLen+rightLen+1)
        return max(leftLen, rightLen)+1
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pathLen(root)
        return max(0, self.maxLen-1)
        
        
