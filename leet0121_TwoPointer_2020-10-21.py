class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1:
            return 0
        i, j = 0,1
        maxProfit = 0
        while(j<len(prices)):
            if prices[j]<=prices[i]:
                i = j
                j += 1
            else:
                maxProfit = max(maxProfit, prices[j]-prices[i] )
                j += 1
        return maxProfit
                
