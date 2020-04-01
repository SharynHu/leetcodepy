# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        stack = []
        s = '('+s+')'
        sign = 1
        num = ""
        for char in s:
            #如果char是'('，将原来的数字以及'('放入栈中，并且将数字正负号及数字字符串重置
            if char=='(':
                if num: stack.append(sign*int(num))
                stack.append(char)
                sign = 1
                num = ""
            #如果char是数字字符，将其加入数字数字字符串中
            if char.isdigit():
                num += char
            #如果char是负号，将数字正负号改变
            if char=='-':
                sign = -1
            #如果char是')'开始处理
            if char==')':
                if num:
                    stack.append(sign*int(num))
                    num = ""
                    sign = 1
                poped = []
                while(stack and stack[-1]!='('):
                    poped.append(stack.pop())
                #pop出'('
                stack.pop()
                if poped:
                    rootNode = TreeNode(poped.pop())
                    if poped:
                        rootNode.left = poped.pop()
                        if poped:
                            rootNode.right = poped.pop()
                    stack.append(rootNode)
                
            
        return stack[0]
