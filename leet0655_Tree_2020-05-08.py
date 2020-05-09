# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 先求出这棵树的高度height，那么整个结果矩阵的宽度就是 pow(2,height)-1.
# 如何填充这个矩阵数组呢？要利用每个父节点在下一层的相对位置，是其所有子节点的最中央的特点，用DFS来做。设置每一层的start和end，找到mid的位置放置父节点的值。则左子树在下一层的摆放区间就在start~mid-1，右子树在下一层的摆放区间就在mid+1~end.如此就可以设置递归函数。
class Solution(object):
    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right))+1
    
    def dfs(self, root, res, start, end, row, height):
        if row>=height or start>end or not root:
            return
        #当前的节点应该在res[row]的中间位置
        mid = (start+end)/2
        res[row][mid] = str(root.val)
        #打印左子树
        self.dfs(root.left, res, start, mid-1, row+1, height)
        self.dfs(root.right, res, mid+1, end, row+1, height)
   
        
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        
        height = self.getHeight(root)
        res = [[""]*(2**height-1) for i in range(height)]
        self.dfs(root, res, 0, 2**height-1, 0, height)
        return res
        
        
