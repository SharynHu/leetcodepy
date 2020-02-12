# Two steps for encoding:
# 1. link all the siblings
# 2. connect the head of each child-list to its parent
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
#Approach1: recursion
class Codec:
    def printTree(self,root):
        if not root:
            print None
            return
        self.printTree(root.left)
        self.printTree(root.right)
        
        
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        #termination condition
        if not root:
            return None
        newRoot = TreeNode(root.val)
        if not root.children:
            return newRoot
        
        head = self.encode(root.children[0])
        p = head
        for i in range(1, len(root.children)):
            q = self.encode(root.children[i])
            p.right = q
            p = q
            
        newRoot.left = head
        return newRoot
        
                

    def decode(self, root):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not root:
            return None
        
        # if the current root has no children, simply create a new N-ary node and return it
        if not root.left:
            return Node(root.val,[])
        
        newRoot = Node(root.val, [])
        currChild = root.left
        while(currChild):
            newCurrChild = self.decode(currChild)
            newRoot.children.append(newCurrChild)
            currChild = currChild.right
        
        return newRoot
        