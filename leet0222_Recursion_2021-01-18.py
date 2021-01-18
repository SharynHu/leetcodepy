# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# for a complete binary tree, the left tree is 
class Solution(object):
    def depth(self, root):
        if not root:
            return 0
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        return max(leftDepth, rightDepth)+1
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # first get the depth of two subtrees
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        # for complete trees, there are only two possibilities, either leftDepth==rightDepth or leftDepth>rightDepth
        if leftDepth==rightDepth:
            # this means the left subtree is a perfect binary tree and the right subtree is a complete binary tree.
            leftCount = 2**leftDepth-1
            rightCount = self.countNodes(root.right)
        else:
            # this means the left subtree is a complete binary tree and the right subtree is a perfect subtree
            rightCount = 2**rightDepth-1
            leftCount = self.countNodes(root.left)
        return leftCount+rightCount+1
        
