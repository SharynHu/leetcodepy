# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#迭代对二叉树进行前序遍历
#先访问root节点，在访问期间左子树和右子树
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while(stack):
            currNode = stack.pop()
            res.append(currNode.val)
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)
        return res
