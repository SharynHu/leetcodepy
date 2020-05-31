# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Summary：
# 1.Base case: None is a perfect binary tree;
# 2.If the left subree and right subtree do not have the same depth, then the only possibility for root to be a complete tree is:
#       a. left subtree is  a complete tree;
#       b. right subtree is a perfect tree;
#       c. their depth differ by one;
#   如果左右子树高度不一致，那么只能是左子树是完全二叉树，右子树为完美二叉树并且深度相差为1
# 3.If the left tree and the right tree has the same depth, then the only possibility is:
#       a. left subtree is a perfect tree;
#       b. right subtree is a complete tree;
#   如果左右子树高度一致，那么只能是左子树是完美二叉树，右子树为完全二叉树
class Solution(object):
    def dfs(self, root):
        if not root:
            return True, True, 0
        # if not root.left and not root.right:
        #     return True, True, 1
        leftIsComplete, leftIsPerfect, leftDepth = self.dfs(root.left)
        rightIsComplete, rightIsPerfect, rightDepth = self.dfs(root.right)
        #首先如果两个子树的深度不相等，那么如果右子树必须为完美二叉树并且深度比左子树小1，左子树必须为完全二叉树
        if leftDepth!=rightDepth:
            if leftIsComplete and rightIsPerfect and leftDepth==rightDepth+1:
                return True, False, leftDepth+1
            return False, False, max(leftDepth, rightDepth)+1
        #如果两棵子树高度相等，那么左子树必须为完美二叉树
        if not leftIsPerfect:
            return False, False, leftDepth+1
        #左子树是完美二叉树，且左右子树高度相同
        #check右子树是否是完美二叉树
        if rightIsPerfect:
            return True, True, leftDepth+1
        #check右子树是否是完全二叉树
        if rightIsComplete:
            return True, False, leftDepth+1
        #右子树都不是完全二叉树
        return False, False, leftDepth+1
       
        
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        complete, perfect, depth = self.dfs(root)
        return complete
