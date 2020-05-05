# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        tmp = root
        res = TreeNode(float('inf'))
        while(tmp):
            if tmp.val>p.val:
                if res.val>tmp.val:
                    res = tmp
                #当前的值大于p的话，那么下一个比当前值小且大于p的只能在tmp的左子树上
                tmp = tmp.left
                continue
            if tmp.val<=p.val:
                #当前值小于p的话，那么只能尝试比当前值大的值
                tmp = tmp.right
                continue
        if res.val == float('inf'):
            return None
        return res
        
