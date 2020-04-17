# 本题的基本思想就是将divisor不断用左移的方法乘以2来逼近dividend，然后将dividend减去倍乘之后的divisor，再重复这个过程直至被除数小于除数。记录这个过程中divisor“倍乘”的总次数，即为答案。
class Solution(object):
    def helper(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #这里假设dividend和divisor都是[-2**31+1, 2**31-1]之间的，这样转换进制的时候就不会overflow
        if (dividend>=0 and divisor>0) or (dividend<0 and divisor<0):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        #先找出divisor的上界并记录倍乘次数
        count = 1
        quotient = 1
        while(divisor<dividend):
            count += 1
            divisor <<= 1
            quotient <<= 1
        #现在divisor>=dividend
        res = 0
        for i in range(count):
            #如果当前的divisor比dividend大，那么将当前的divisor右移一位
            if divisor<=dividend:
                res += quotient
                dividend -= divisor
            quotient >>= 1
            divisor >>= 1
        return sign*res
        
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #处理overflow的case
        if dividend == -2**31:
            if divisor == -1:
                #overflow
                return 2**31-1
            if divisor == -2**31:
                return 1
        if divisor == -2**31:
            return 0
        return self.helper(dividend, divisor)
