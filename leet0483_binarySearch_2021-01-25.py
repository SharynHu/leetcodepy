# first convert the string into an integer to make the calculation easy;
# for this problem we need to find a base b such that b**(exp+1)-1)/(b-1)==n
# To solve this problem we can loop through all possible exponents(because the range of exponents is relatively smaller)
# and to find the corresponding base for each exponent, we use binary search.
# since 1+b+b^2+...+b^exp=n. it means n>b^exp, so b<pow(n,1.0/exp)
class Solution(object):
    def check(self, exp, n):
        #check if we can find a base for this exponent sych that b**(exp+1)-1)/(b-1)==n
        left, right = 2, int(math.pow(n, 1.0/exp))+1
        while(left<=right):
            middle = (left+right)/2
            curr = 1
            for i in range(exp+1):
                curr *= middle
                if curr>(n+1)*(middle-1):
                    right = middle-1
                    break
            if curr==n*(middle-1)+1:
                return middle
            if curr<n*(middle-1)+1:
                left = middle+1
            else:
                right = middle-1
        return 0
        
        
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        # The smallest base is 2
        for exp in range(int(math.log(n, 2))+1, 1, -1):
            base = self.check(exp,n)
            if base:
                return str(base)
        return str(n-1)
        
