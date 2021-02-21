class Solution(object):
    def check(self, bloomDay, m, k, candidate):
        count = 0
        res = 0
        for i in range(len(bloomDay)):
            if count==k:
                res += 1
                count=0
            if bloomDay[i]>candidate:
                count = 0
                continue
            count += 1

        if count==k:
            res += 1
        return res>=m
    
    
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(bloomDay)<m*k:
            return -1
      
        left = 0
        right = max(bloomDay)
         
        while(left+1<right):
            middle = (left+right)/2
            if self.check(bloomDay, m, k, middle):
                right = middle
            else:
                left = middle

        if self.check(bloomDay, m, k, left):
            return left
        return right
