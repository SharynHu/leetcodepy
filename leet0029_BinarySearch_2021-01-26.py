# No using multiplication, division, and mod operator, which means we can only use bit manipulation.
class Solution(object):
    def helper(self, dividend, divisor):
        # we set the initialization of right as one
        count = 0 
        while(dividend>0):
            right = 0
            # print dividend, right, dividend-divisor<<right
            while(dividend-(divisor<<right)>=0):
                right += 1
            # print dividend, right, dividend-divisor<<right
            # now dividend<divisor*(2^right)
            if right==0:
                return count
            count += 1<<(right-1)
            dividend -= divisor<<(right-1)
            right = 0
        return count
                
        
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -(1<<31):
                return (1<<31)-1
            else:
                return -dividend
        if dividend == 0:
            return 0
        
        if dividend>0 and divisor>0 or (dividend<0 and divisor<0):
            sign = 1
        else:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        return sign*self.helper(dividend, divisor)
        
