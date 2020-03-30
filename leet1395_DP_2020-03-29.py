class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        if not rating or len(rating)<3:
            return 0
        #dp1[i][j]表示以i结尾长度为j的递增子序列的个数,这里我们只考虑长度为0-3的
        dp1 = [[0]*(len(rating)) for i in range(4)]
        dp1[1] = [1]*len(rating)
        #dp12[i][j]表示以i结尾长度为j的递减子序列的个数,这里我们只考虑长度为0-3的
        dp2 = [[0]*(len(rating)) for i in range(4)]
        dp2[1] = [1]*len(rating)
        
        for i in range(len(rating)):
            for j in range(i):
                if rating[i]>rating[j]:
                    dp1[2][i] += dp1[1][j]
                    dp1[3][i] += dp1[2][j]
                if rating[i]<rating[j]:
                    dp2[2][i] += dp2[1][j]
                    dp2[3][i] += dp2[2][j]
        return sum(dp1[3])+sum(dp2[3])
