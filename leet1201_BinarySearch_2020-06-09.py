class Solution(object):
    def gcd(self, a, b):
        if a<b:
            return self.gcd(b,a)
        if b==0:
            return a
        return self.gcd(b, a%b)
    
    
    def lcm(self, a, b):
        return a*b/self.gcd(a, b)
    
    
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ab = self.lcm(a, b)
        bc = self.lcm(b, c)
        ac = self.lcm(a, c)
        abc = self.lcm(a, bc)
        
        start = 0
        end = a*n
        
        while(start<end):
            middle = (start+end)/2
            #计算分别能被a,b,c, ab, bc, ac, abc整除的数的个数
            count_a, count_b, count_c, count_ab, count_bc, count_ac, count_abc = middle/a, middle/b, middle/c, middle/ab, middle/bc, middle/ac, middle/abc
            totalCount = count_a+count_b+count_c-count_ab-count_bc-count_ac+count_abc
            if totalCount>n:
                end = middle-1
            if totalCount<n:
                start = middle+1
            #相等的话要继续向左边寻找更小的值
            if totalCount==n:
                end = middle
        return start
