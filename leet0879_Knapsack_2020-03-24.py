class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        #dp[j][k] means the number of ways to use j people generating at least profit k
        dp = [[0]*(P+1) for j in range(G+1)]
        dp[0][0] = 1
        for i in range(1, len(group)+1):
            for j in range(G, -1, -1):
                for k in range(P, -1, -1):
                    #if we do not commit crime i-1, then we must get at least profit k choosing from crimes[:i-1] using people j
                    # if we commit crime i-1, then we must achieve at least profit k-profit[i-1] from crimes[:i-1] using people j.
                    # noting that if k-profit[i-1]<0, then we can achieve at least profit 0 from crimes[:i-1] using people j.
                    if j-group[i-1]>=0:
                        dp[j][k] += dp[j-group[i-1]][max(k-profit[i-1],0)]
        
        res = 0
        for j in range(G+1):
                res += dp[j][P]
        return res%(10**9+7)
