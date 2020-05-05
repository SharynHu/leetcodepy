# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#中序遍历该BST，看数据是否有序
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [root]
        prevVal = float('-inf')
        while(stack):
            while(stack[-1].left):
                stack.append(stack[-1].left)
            
            #Now the top node does not have a left tree
            while(stack):
                currNode = stack.pop()
                if currNode.val<= prevVal:
                    return False
                prevVal = currNode.val
                if currNode.right:
                    stack.append(currNode.right)
                    break
        return True
