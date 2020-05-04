# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, inorder, inStart, inEnd, postorder, postStart, postEnd, valToIndex):
        if inStart>inEnd or postStart>postEnd:
            return None
        rootVal = postorder[postEnd]
        rootNode = TreeNode(rootVal)
        #root节点的index为
        index = valToIndex[rootVal]
        #那么左子树的中序为
        leftInStart, leftInEnd = inStart, index-1
        #右子树的中序为
        rightInStart, rightInEnd = index+1, inEnd
        #左子树的后序为
        leftPostStart, leftPostEnd = postStart, postStart+(leftInEnd-leftInStart)
        #右子树的后序为
        rightPostStart, rightPostEnd = leftPostEnd+1, postEnd-1
        rootNode.left = self.dfs(inorder, leftInStart, leftInEnd, postorder, leftPostStart, leftPostEnd, valToIndex)
        rootNode.right = self.dfs(inorder, rightInStart, rightInEnd, postorder, rightPostStart, rightPostEnd, valToIndex)
        return rootNode
        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        valToIndex = {}
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i
        return self.dfs(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, valToIndex)
            
