# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#思路：用栈中序遍历BST
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        
        count = 0
        while(stack):
            #如果当前节点有左子树，那么开始访问其左子树
            while(stack and stack[-1].left):
                stack.append(stack[-1].left)
            #当前节点无左子树，开始访问
            while(stack):
                currNode = stack.pop()
                count += 1
                if count==k:
                    return currNode.val
                #如果当前节点有右子树，那么在访问完当前节点之后应该访问其右子树
                if currNode.right:
                    stack.append(currNode.right)
                    break
                #如果当前节点没有右子树， 那么继续访问
