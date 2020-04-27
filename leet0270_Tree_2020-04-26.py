# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        p = root
        closest = root.val
        
        while(p):
            if p.val == target:
                return p.val
            if abs(p.val-target)<abs(closest-target):
                closest = p.val
            #比较当前值和target的大小
            if p.val>target:
                p = p.left
            else:
                p = p.right
        return closest
