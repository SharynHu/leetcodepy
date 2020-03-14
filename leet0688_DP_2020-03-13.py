class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = collections.defaultdict(float)
        dp[(r, c)] = 1
        for k in range(K):
            newDp = collections.defaultdict(float)
            for i, j in list(dp):
                for m, n in [(i-1, j-2), (i-2, j-1), (i-2, j+1), (i-1, j+2), (i+1, j-2), (i+1, j+2), (i+2, j-1), (i+2, j+1)]:
                    if 0<=m<N and 0<=n<N:
                        newDp[(m,n)] += dp[(i, j)]*0.125
            dp = newDp
        return sum(dp.values())
