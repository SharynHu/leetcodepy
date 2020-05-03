# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#以高度为-1来denote某个节点是unbalanced
class Solution(object):
    def getHeight(self, root):
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight-rightHeight)>1:
            return -1
        return max(leftHeight, rightHeight)+1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height = self.getHeight(root)
        if height==-1:
            return False
        return True
