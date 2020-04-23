#思路：筛去所有已知质数的倍数
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        #首先标记所有数为质数
        isPrime = [True]*(n)
        isPrime[0] = False
        isPrime[1] = False
        
        for i in range(2,int(math.ceil(math.sqrt(n)))+1):
            #如果当前的数是质数，将count+1
            if isPrime[i]:
                j = 2
                while(i*j<n):
                    isPrime[i*j] = False
                    j += 1
        count = 0
        for i in range(n):
            if isPrime[i]:
                count += 1
        return count
