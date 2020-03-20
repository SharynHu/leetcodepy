class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 3:
            return N
        #dp[i][j] means the maximun "A" printed for operation i
        dp = [[0]*(N+1) for i in range(4)]
        #对于CTRL+V来说，由于直接与原来
        for i in range(1, N+1):
            #如果当前操作是A
            # print i, max([dp[0][i-1], dp[1][i-1], dp[2][i-1], dp[3][i-1]])
            dp[0][i] = max([dp[0][i-1],dp[1][i-1], dp[2][i-1], dp[3][i-1]])+1
            #如果当前操作是CTRL+A
            dp[1][i] = max([dp[0][i-1], dp[2][i-1], dp[3][i-1]])
            #如果当前操作是CTRL+C，那么之前的操作一定是CTRL+A
            dp[2][i] = dp[1][i-1]
            #如果当前操作是CTRL+V，那么前一步为CTRL+C或者CTRL+V，那么现在就要知道step到底是多少。
            #如果操作i-1是CTRL+C的话，那么很简单， dp[3][i] = 2*dp[2][i-1]
            #如果操作i-1是CTRL+V的话，那么我们需要知道到底paste了多少。
            #如果操作i-2是CTRL+C的话，那么dp[3][i-1] = 2*dp[2][i-2]
            #如果操作i-2是CTRL+V的话，那么i-2是paste的某一次CTRL+C的值，那么我们可以从第一次CTRL开始寻找，剩下的次数全部都是CTRL+V(这样才能最大化现在的“A”的个数)
            for j in range(1, i):
                dp[3][i] = max(dp[3][i], dp[2][j]*(i-j+1))
            # print dp[0]
        return max([dp[0][-1], dp[1][-1], dp[2][-1], dp[3][-1]])
