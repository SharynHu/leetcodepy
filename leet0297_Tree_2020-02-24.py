# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Approach1:
#     BFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        queue = collections.deque([root])
        while(queue):
            currNode = queue.pop()
            if not currNode:
                nodes.append(None)
                continue
            nodes.append(currNode.val)
            queue.appendleft(currNode.left)
            queue.appendleft(currNode.right)
        return nodes
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = data.pop(0)
        if root==None:
            return None
        root = TreeNode(root)
       
        parent = [root]
        while(data):
            size = len(parent)
            for i in range(size):
                currNode = parent.pop(0)
                left = data.pop(0)
                right = data.pop(0)
                if left!=None:
                    left = TreeNode(left)
                    parent.append(left)
                if right!=None:
                    right = TreeNode(right)
                    parent.append(right)
                currNode.left = left
                currNode.right = right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
