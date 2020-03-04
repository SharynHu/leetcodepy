class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A or not A[0]:
            return 0
        
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                tmp = A[i-1][j]
                if j-1>=0:
                    tmp = min(tmp, A[i-1][j-1])
                if j+1<len(A[0]):
                    tmp = min(tmp, A[i-1][j+1])
                A[i][j] = tmp+A[i][j]
        return min(A[-1])
