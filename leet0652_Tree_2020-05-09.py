# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#使用哈希来判断两个子树是否相等
class Solution(object):
    def serialize(self, root, hashMap):
        if not root:
            return "null"
        left = self.serialize(root.left, hashMap)
        right = self.serialize(root.right, hashMap)
        curr = str(root.val)+left+right
        hashMap[curr].append(root)
        return curr
    
    
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        hashMap = collections.defaultdict(list)
        self.serialize(root, hashMap)
        res = []
        for val in hashMap:
            print [node.val for node in hashMap[val]]
            if len(hashMap[val])>=2:
                res.append(hashMap[val][0])
        return res
