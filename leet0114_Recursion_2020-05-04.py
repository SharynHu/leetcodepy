# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left:
            self.flatten(root.right)
            return
        if not root.right:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            return 
        self.flatten(root.left)
        self.flatten(root.right)
        #找到左子树最右边的节点
        p = root.left
        while(p.right):
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None
        return root
        
