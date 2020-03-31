# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        if root:
            stack.append(root)
            
        while(stack):
            #如果栈顶节点右左子树，先访问左子树
            while(stack[-1].left):
                stack.append(stack[-1].left)
            while(stack):
                #该节点没有左子树，开始访问该节点
                currNode = stack.pop()
                res.append(currNode.val)
                #如果该节点有右子树，需要在访问完该节点后访问其右子树
                if currNode.right:
                    stack.append(currNode.right)
                    break
        return res
                
