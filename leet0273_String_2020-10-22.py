# 2^31-1==2,147,483,647, 也就是说num应该是billion级别，再往上的不用考虑了。
# 因此num函数分6个部分处理， bililon, million, thousand, hundred, tens 以及 ones.
# 注意对于tens有一部分特殊的数从10-20。
class Solution(object):
    def __init__(self):
        #initializing all the needed global mappings.
        self.ones = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
        self.tensLessThan20 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        self.tens = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
    
    def one(self, num):        
        return self.ones[num]
    
    def two(self, num):
        if not num:
            return ""
        if 0<num<10:
            return self.one(num)
        if 10<=num<20:
            return self.tensLessThan20[num]
        if num%10==0:
            return self.tens[num/10]
        else:
            return self.tens[num/10]+" "+self.one(num%10)
        
    def three(self, num):
        hundred = num/100
        rest = num%100
        # print hundred, rest
        if hundred and rest:
            return self.one(hundred) + " Hundred "+self.two(rest) 
        if not hundred and rest:
            return self.two(rest)
        if not rest:
            return  self.one(hundred) + " Hundred"
        return ""
        
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        
        result = ""
        #将num分为四个部分，billion, million, thousand和其他部分
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        if billion:
            result = self.three(billion)+" Billion"
        if million:
            result += " " if result else ""
            result += self.three(million)+" Million"
        if thousand:
            result += " " if result else ""
            result += self.three(thousand)+" Thousand"
        if rest:
            result += " " if result else ""
            result += self.three(rest)
        return result
        
