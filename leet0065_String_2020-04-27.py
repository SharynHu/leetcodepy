# 本题的主框架是找到科学记数法的标记“e”。“e”之前和之后的两个子字符串必须分别都是合法的“数”。但是“e”之前的子字符串允许是一个小数，后者只允许是整数。
# 合法的小数的定义是：数字+最多一个小数点。合法的整数的定义是：数字+没有小数点。
# 任何正负号，只可能出现在合法的数（无论整数或小数）的第一个字符的位置。
# 可能需要单独判断的corner cases是：只有小数点或空或“e”的字符串都不是合法的数
class Solution(object):
    def isInteger(self, t):
        '''
        判断一个无符号数是不是整数
        '''
        if not t:
            return False
        for i in range(len(t)):
            if not t[i].isdigit():
                return False
        return True
    
    def isDecimal(self, t):
        '''
        判断一个无符号数是不是小数
        '''
        tList = t.split('.')
        "如果不含小数点或者含有多个小数点"
        if len(tList)==1 or len(tList)>=3:
            return False
        s1 = tList[0]
        s2 = tList[1]
        #对于小数来说，左右两边都是整数
        if not s1:
            return self.isInteger(s2)
        if not s2:
            return self.isInteger(s1)
        return self.isInteger(s1) and self.isInteger(s2)
    
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #step1:去掉字符串开头结尾的空格
        s = s.strip()
        if not s:
            return False
        #step2根据e来split当前的数
        sList = s.split('e')
        
        #如果当前数字没有使用科学计数法
        if len(sList) ==1:
            s = sList[0]
            if not s:
                return False
            #去掉符号
            if s[0] == '+' or s[0]=='-':
                s = s[1:]
            return self.isInteger(s) or self.isDecimal(s)
        #如果含有两个"e"
        if len(sList)>=3:
            return False
        #如果当前数字使用科学计数法，那么左边可以是小数或者整数，右边必须是整数
        s1 = sList[0]
        s2 = sList[1]
        if not s1 or not s2:
            return False
        #去掉符号
        if s1[0] == '+' or s1[0] == '-':
            s1 = s1[1:]
        if s2[0] == '+' or s2[0] == '-':
            s2 = s2[1:]
        return (self.isInteger(s1) or self.isDecimal(s1)) and self.isInteger(s2)
