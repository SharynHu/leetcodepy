class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        res = []
        while(i<=j):
            if A[i]**2>=A[j]**2:
                res.append(A[i]**2)
                i += 1
            else:
                res.append(A[j]**2)
                j -= 1
        res.reverse()
        return res
                
