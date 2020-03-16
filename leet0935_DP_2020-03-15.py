class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==1:
            return 10
        
        #dp[i][j]表示第j步后处于位置i所拥有的不同的dial数
        dp = [[0]*N for i in range(10)]
        # 初始化
        for i in range(10):
            dp[i][0] = 1
           
        transferMatrix = {1:[8,6], 2:[7,9], 3:[4,8], 4:[3,9,0], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2,4], 0:[4,6]}
        for j in range(1, N):
            for i in range(10):
                for k in transferMatrix[i]:
                    dp[i][j] += dp[k][j-1]
                dp[i][j] %=10**9+7

        return sum([dp[i][-1] for i in range(10)])%(10**9+7)
