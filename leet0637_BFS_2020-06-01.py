# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while(queue):
            size = len(queue)
            currSum = 0
            for i in range((size)):
                curr = queue.pop()
                currSum += curr.val
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
            res.append(currSum/float(size))
        return res
