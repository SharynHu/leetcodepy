#将分数转换为（无限循环小数）
#难点：找到重复的分母
#思路， 使用hashmap
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if (numerator>=0 and denominator>0) or  (numerator<=0 and denominator<0):
            sign = 1
        else:
            sign = -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        res = ""
        #先计算整数部分
        res += str(numerator/denominator)
        if numerator%denominator==0:
            res = res if sign==1 else "-"+res
            return res
        res += "."
        numerator = 10*(numerator%denominator)
        #seen记录该numerator第一次出现所对应的商的index
        seen = {}
        while(numerator>0):
            seen[numerator] = len(res)
            res += str(numerator/denominator)
            numerator = (numerator%denominator)*10
            if not numerator:
                res = res if sign==1 else "-"+res
                return res
            if numerator in seen:
                index = seen[numerator]
                res = res[:index]+"("+res[index:]+")"
                res = res if sign==1 else "-"+res
                return res
