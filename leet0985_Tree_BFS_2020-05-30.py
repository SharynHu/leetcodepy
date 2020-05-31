# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Summary：
#层序遍历所有的节点
#当我们碰到第一个null节点之后所有遇到的节点都必须是null节点
class Solution(object):   
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = collections.deque([root])
        level = 0
        
        #END means that we've met the first NULL node.
        END = False
        while(queue):
            size = len(queue)
            for i in range(size):
                curr = queue.pop()
                #如果之前还没有遇到NULL节点
                if not END:
                    #如果当前节点是NULL节点， 那么update END的值
                    if not curr:
                        END = True
                        continue
                    #如果当前节点不是NULL节点，将其左右子树进栈
                    queue.appendleft(curr.left)
                    queue.appendleft(curr.right)
                    continue
                #如果之前已经遇到过NULL节点了，那么当前节点只能是NULL节点
                if curr:
                    return False
        return True
