# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#比较左右两棵树的深度，如果左子树的深度等于右子树的深度，那么说明左子树是完美二叉树，右子树是完全二叉树
#如果左子树的高度大于右子树的高度，说明左子树是完全二叉树，右子树是完美二叉树
#这样就构成了一个递归的结构

class Solution(object):
    def getHeight(self, root):
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        return leftHeight+1
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight==rightHeight:
            #说明左子树是完美二叉树，右子树是完全二叉树
            return 2**leftHeight+self.countNodes(root.right)
        else:
            #说明左子树是完全二叉树，右子树是完美二叉树
            return 2**rightHeight+self.countNodes(root.left)
