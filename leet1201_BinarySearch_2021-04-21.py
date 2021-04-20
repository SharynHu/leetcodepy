class Solution(object):
    def gcd(self, a, b):
        if a<b:
            return self.gcd(b,a)
        if not b:
            return a
        return self.gcd(a%b, b)
    
    def lcm(self, a, b):
        return a*b/(self.gcd(a,b))
    
    def count(self, n, a,b,c,ab,bc,ac,abc):
        return n/a+n/b+n/c-n/ab-n/bc-n/ac+n/abc
    
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ab = self.lcm(a,b)
        ac = self.lcm(a,c)
        bc = self.lcm(b,c)
        abc = self.lcm(self.lcm(a,b),c)
        
        left = 0
        right = a*n
        
        while(left+1<right):
            middle = (left+right)/2
            count = self.count(middle, a,b,c,ab,bc,ac,abc)
            if count>=n:
                right = middle
            else:
                left = middle
        if self.count(left, a,b,c,ab,bc,ac,abc)==n:
            return left
        return right
