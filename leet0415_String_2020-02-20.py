#记录每一位数字，最后组合起来

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #preprocess 
        if len(num1)>len(num2):
            num1, num2 = num2, num1
        
        digits = []
        carry = 0
        i=1
        while(i<=len(num1)):
            sum_ = int(num1[-i])+int(num2[-i])+carry
            digits.append(sum_%10)
            carry = sum_/10
            i += 1
            
        while(i<=len(num2)):
            sum_ = int(num2[-i])+carry
            digits.append(sum_%10)
            carry = sum_/10
            i += 1
        
        if carry:
            digits.append(carry)
        
        res = ""
        for i in range(len(digits)):
            res = str(digits[i])+res
        return res
