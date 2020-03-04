# For each day, if you don't have to travel today, then it's strictly better to wait to buy a pass. If you have to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or 30-day pass.
# We can express those choices as a recursion and use dynamic programming. Let's say dp(i) is the cost to fulfill your travel plan from day i to the end of the plan. Then, if you have to travel today, your cost is:
#dp(i)=min(dp(i-1)+costs[0],dp(i-7)+costs[1],dp(i-30)+costs[2])
class Solution(object):
    def mincostTickets(self, days, cost):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        daySet = set(days)
        dp = [0]*366
        
        for i in range(1, 366):
            if i not in daySet:
                #今天不出门无需用票
                dp[i] = dp[i-1]
            else:
                #今天要出门，需要用票
                # 1. 使用1-day ticket
                dp[i] = dp[i-1]+cost[0]
                
                # 2. 使用7-day ticket,那么现在的票必定在7天票的有效期内，可能是第i-6, i-5...i-1, i天买的， 那么
                # dp[i] = min(dp[i-7], dp[i-6], dp[i-5], ..., dp[i-1])+cost[1]
                # 考虑到dp[i]为递增序列， 那么最小值为dp[i-7]+cost[1]
                # 还要考虑到i-7<0的情况，此时只有今天可以买7-day ticket， 那么dp[i] = cost[1]
                if i>=8:
                    dp[i] = min(dp[i], dp[i-7]+cost[1])
                else:
                    dp[i] = min(dp[i], cost[1])
                
                # 3. 使用30-day ticket,同上
                if i>=31:
                    dp[i] = min(dp[i], dp[i-30]+cost[2])
                else:
                    dp[i] = min(dp[i], cost[2])
        return dp[-1]
