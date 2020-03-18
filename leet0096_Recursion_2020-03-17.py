class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        # choose one from n to be the root, there are n possibilities
        res = 0
        for i in range(2, n):
            res += self.numTrees(i-1)*self.numTrees(n-i)
        return res+self.numTrees(n-1)*2
