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
            #step1: if stack is not empty and the top node has a left child, we push the left child into the stack; else, we go to step 2
            while(stack and stack[-1].left):
                stack.append(stack[-1].left)
                
            #step2: if the stack is not empty, we pop out the top node. if the top node has a right child, we push it into the stack then go to step 1; else we continue
            while(stack):
                currNode = stack.pop()
                if not currNode.val>prevVal:
                     return False
                prevVal = currNode.val
                if not currNode.right:
                    continue
                stack.append(currNode.right)
                break

        return True
