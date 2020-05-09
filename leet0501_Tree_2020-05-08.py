# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#中序遍历BST
class Solution(object):
    def __init__(self):
        self.maxCnt = 0
        self.res = []
        self.count = 0
        self.prev = None
        
    def inorder(self, root):
        if not root:
            return 
        #访问左子树
        self.inorder(root.left)
        #访问当前节点
        if not self.res:
            self.count = 1
            self.prev = root.val
            self.res = [root.val]
        else:
            if root.val == self.prev:
                self.count += 1
            else:
                if self.count>self.maxCnt:
                    self.maxCnt = self.count
                    self.res = [self.prev]
                elif self.count==self.maxCnt:
                    self.res.append(self.prev)
                self.count = 1
                self.prev = root.val
        self.inorder(root.right)
                      
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.inorder(root)
        if self.count>self.maxCnt:
            self.maxCnt = self.count
            self.res = [self.prev]
        elif self.count==self.maxCnt:
            self.res.append(self.prev)
        return self.res
