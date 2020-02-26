class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost or len(cost)==0:
            return 0
        if len(cost)==1:
            return cost[0]
        if len(cost)==2:
            return min(cost)
        # dp[i] means the minimum cost to reach index i
        dp = [0, 0]
        for i in range(2, len(cost)):
            dp.append(min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1]))
        
        return min(dp[-2]+cost[-2], dp[-1]+cost[-1])
            
