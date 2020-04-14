class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        if not customers:
            return 0
        
        part1 = 0
        part2 = sum(customers[:X] or [0])
        part3 = sum([customers[i]*(1-grumpy[i]) for i in range(X, len(customers))])
        res = part1+part2+part3
        for i in range(1, len(customers)-X+1):
            # we move the window 1 step forward
            part1 += customers[i-1]*(1-grumpy[i-1])
            part2 += customers[i+X-1]-customers[i-1]
            part3 -= customers[i+X-1]*(1-grumpy[i+X-1])
            res = max(res, part1+part2+part3)
        return res
        
