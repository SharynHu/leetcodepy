#Approach1, stack中放置元素名及其个数, 最后将所有的dict都concate起来
#formula中存在的字符
#1.左括号:说明我们要开始一个subformula
#2.大写字母：说明要开始一个新元素
#3.小写字母：跟在大写字母后面，于大写字母一起组成一个元素名
#4.数字：跟在元素/subformula后面，表示这个元素/subformula的个数
#5.右括号：表示一个subformula的结束，后面跟数字

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = []
        formula = ('('+formula+')')[::-1]
        elemName = ""
        num = ""
        for char in formula:
            if char == ')':
                stack.append(1 if not num else int(num))              
                stack.append(char)
                #重置elemName and num
                elemName = num = ""
            if char.isdigit():
                num = char+num
            if char.islower():
                #开始元素名
                elemName = char+elemName
            if char.isupper():
                #结束元素名
                elemName = char+elemName
                # 将元素名和元素个数一起压入栈中
                stack.append(1 if not num else int(num))    
                stack.append(elemName)
                #重置num和元素名
                elemName = num = ""
            if char =='(':
                #开始处理
                count = collections.defaultdict(int)
                while(stack and stack[-1]!=')'):
                    name = stack.pop()
                    count[name] += stack.pop()
                #pop out ')'
                stack.pop()
                #pop out the occurance of this subformula
                occur = stack.pop()
                for name in count.keys():
                    stack.append(count[name]*occur)
                    stack.append(name)
                #重置num和元素名
                elemName = num = ""
            
        counts = collections.defaultdict(int)
        while(stack):
            name = stack.pop()
            counts[name] += stack.pop()
        res = ""
        for name in sorted(counts.keys()):
            res += (name+"") if counts[name]==1 else (name+str(counts[name]))
        return res
                
