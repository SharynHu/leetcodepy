class Solution(object):
    def gcd(self, a, b):
        if a<b:
            return self.gcd(b,a)
        if not b:
            return a
        return self.gcd(a%b, b)
    
    def lcm(self, a, b):
        return a*b/self.gcd(a,b)
    
    
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        lcm_ab = self.lcm(a, b)
        lcm_ac = self.lcm(a, c)
        lcm_bc = self.lcm(b, c)
        lcm_abc = self.lcm(a, lcm_bc)
        
        left = 0
        right = a*n
        while(left+1<right):
            middle = (left+right)/2
            # check if middle is the n-th ugly number
            rank = middle/a+middle/b+middle/c-middle/lcm_ab-middle/lcm_bc-middle/lcm_ac+middle/lcm_abc
            if rank<n:
                left = middle
            else:
                right = middle
        # print left, right
        if (left/a+left/b+left/c-left/lcm_ab-left/lcm_bc-left/lcm_ac+left/lcm_abc==n):
            return left
        return right
