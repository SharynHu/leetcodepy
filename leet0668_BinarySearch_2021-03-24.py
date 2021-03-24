class Solution(object):
    def count(self, m, n, candidate):
        '''
        count how many numbers that are less than or equal to candidate
        '''
        count = 0
        j = n
        for i in range(1, m+1):
            while(j>=1 and i*j>candidate):
                j -= 1
            count += j
        return count
        
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left = 1
        right = m*n
        
        while(left+1<right):
            middle = (left+right)/2
            if self.count(m,n,middle)>=k:
                right = middle
            else:
                left = middle
        if self.count(m,n,left)>=k:
            return left
        return right
