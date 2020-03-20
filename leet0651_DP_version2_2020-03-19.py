#keypoint:要最大化"A"的个数，如果要执行CTRL+V， 那么这个顺序一定是CTRL+A, CTRL+C,  CTRL+V, CTRL+V....
#也就是说CTRL+V一定是放在后面的
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        dp = [0]*(N+1)
        for i in range(1, N+1):
            for j in range(i):
                #如果当前是CTRLA+CTRLC+CTRV...
                if i-j >=3:
                    dp[i] = max(dp[i], dp[j]*(i-j-1))
                dp[i] = max(dp[i], dp[j]+i-j)
        return dp[-1]
                    
