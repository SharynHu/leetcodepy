"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        #如果两棵树中有一个是叶节点，说明该树的所有的值都是一样的，此时两树相或的值可以确定
        if quadTree1.isLeaf: return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf: return quadTree2 if quadTree2.val else quadTree1
        
        # 两个树都不是叶节点，需要递归计算结果。
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        #比较四个node的值是否相同
        if topLeft.val==topRight.val==bottomLeft.val==bottomRight.val and topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
            return Node(topLeft.val, 1,  None, None, None, None)
        return Node(0, 0, topLeft, topRight, bottomLeft, bottomRight)
