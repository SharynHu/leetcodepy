class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        #stack中存放需要删除的左括号"("地址
        #indice_to_remove中存放需要删除的右括号地址
        stack = []
        indice_to_remove  = set()
        
        for i, char in enumerate(s):
            if char not in "()":
                continue
            if char=="(":
                stack.append(i)
                continue
            # currently char==")"
            if not stack:
                #说明当前栈中没有"("与其匹配， 需要将其加入indice_to_remove
                indice_to_remove.add(i)
            else:
                #栈中有一个左括号与其匹配，将该左括号从待删除的栈中弹出
                stack.pop()
        indice_to_remove = indice_to_remove.union(set(stack))
        validStr = ""
        for i in range(len(s)):
            if i not in indice_to_remove:
                validStr += s[i]
        return validStr
