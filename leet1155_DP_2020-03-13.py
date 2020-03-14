# As an initial example, pretend we have 5 dice with 6 faces each and we want to determine how many ways to make 18.
# In other words, what is dp(5, 6, 18)?

# At first glance, this is seems difficult and overwhelming. But if we make one simple observation, we can reduce this big problem into several smaller sub-problems. We have 5 dice, but let's first just look at ONE of these dice (say the last one). This die can take on f different values (1, ... , f), so we can consider what happens when we fix its value to any of these possibilities. In this case, f= 6.

# Case 1: The last die is a 1. The remaining 4 dice must sum to 18-1=17. This can happen dp(4, 6, 17) ways.
# Case 2: The last die is a 2. The remaining 4 dice must sum to 18-2=16. This can happen dp(4, 6, 16) ways.
# Case 3: The last die is a 3. The remaining 4 dice must sum to 18-3=15. This can happen dp(4, 6, 15) ways.
# Case 4: The last die is a 4. The remaining 4 dice must sum to 18-4=14. This can happen dp(4, 6, 14) ways.
# Case 5: The last die is a 5. The remaining 4 dice must sum to 18-5=13. This can happen dp(4, 6, 13) ways.
# Case 6: The last die is a 6. The remaining 4 dice must sum to 18-6=12. This can happen dp(4, 6, 12) ways.

# dp(5, 6, 18) = dp(4, 6, 17) + dp(4, 6, 16) + dp(4, 6, 15) + dp(4, 6, 14) + dp(4, 6, 13) + dp(4, 6, 12)

# We sum up the solutions for each of these 6 cases to arrive at our result. Of course, each of these cases branches off into 6 cases of its own, and the recursion only resolves when d=0. 

#Suppose dp[i][j] means number of ways we can get exactly sum j using i dice. then, 
#dp[i][j] = dp[i-1][1]+dp[i-1][2]+...+dp[i-1][j-1]

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        dp = [[0]*(target+1) for i in range(d+1)]
        #Initialization
        for j in range(1, target+1):
            if j<=f:
                dp[1][j] = 1
        
        for i in range(2, d+1):
            for j in range(2, target+1):
                if i*f<j or i>j:
                    dp[i][j] = 0
                    continue
                for k in range(1, min(f+1, j)):
                    dp[i][j] += (dp[i-1][j-k])%(10**9+7)

        return (dp[-1][-1])%(10**9+7)
