# Given an interger x, how many number od zeros x! has at the end of it is decided by how many 5s it has in its factorization.

# An observation:
#     Suppose we have an interger x1, where x1 is the smallest number with x! having k leading integers. For example, for numbers having a factorization with 0 tailing zeroes, which are 0!,1!,2!,3!,4!, 0 is the smallest among them. For numbers having a factorization with 1 leading zeros, which are 5!,6!,7!,8!,9!, 5 is the smallest among them. So we can see that x1%5==0, and for every 5 numbers, we must add at least one tailing zero. x1!, (x1+1)!,(x1+2)!,(x1+3)!,(x1+4)!, they must have the same number of tailing zeroes as x1!, so there are at least 5 numbers having k tailing zeroes. And for (x1+5)!, it must be divided by 5, so it has at least k+1 tailing zeroes. So  there are at most 5 numbers having k tailing zeroes. 
#    So the conclusion is if we can find a number x! having k tailing zeroes, then there must be 4 more numbers having k tailing zeroes. If we cannot find such x!, then there is 0 such numbers with a factorization having k tailing zeroes.

class Solution(object):
    def countTailingZeroes(self, n):
        res = 0
        while(n):
            res += n/5
            n /= 5
        return res
    
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        
        left = 0
        right = 5*(K+1)
        while(left+1<right):
            middle = (left+right)/2
            if self.countTailingZeroes(middle)<=K:
                left = middle
            else:
                right = middle
        if self.countTailingZeroes(left)==K or self.countTailingZeroes(right)==K:
            return 5
        return 0
