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
#Approach2: BFS
from collections import deque
class Codec:
        
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        newRoot = TreeNode(root.val)
        queue = deque([(newRoot, root)])
        while(queue):
            parent, curr = queue.popleft()
            #build a dummy head for the child list
            dummy = TreeNode(0)
            p = dummy
            for child in curr.children:
                #construct the newChild
                newChild = TreeNode(child.val)
                #link all the new children
                p.right = newChild
                p = p.right
                #add the newChild and the old child into the queue
                queue.append((newChild, child))
            
            # set the head of the children list as the left child of the parent
            parent.left = dummy.right
        return newRoot
                

    def decode(self, root):
        """Decodes your binary tree to an n-ary tree.
        :type root: TreeNode
        :rtype: Node
        """
        if not root:
            return None
        
        # if the current root has no children, simply create a new N-ary node and return it
        if not root.left:
            return Node(root.val,[])
        
        newRoot = Node(root.val, [])
        queue = deque([(newRoot, root)])
        while(queue):
            parent, curr = queue.popleft()
            head = curr.left
            while(head):
                newChild = Node(head.val, [])
                parent.children.append(newChild)
                queue.append((newChild, head))
                head = head.right
        return newRoot