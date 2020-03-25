#The difference ranges from [min(A)-max(A), max(A)-min(A)]
#so we need to build a 2-D dp matrix that is dp[:len(A)][:2*MAXDIF+1]
class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        
        #dp[(i,j)] means the maximum length for a subsequence ending with index i and having step j
        dp = {}
        
        maxLen = 1
        for i in range(len(A)):
            for j in range(i):
                dp[(A[i], A[i]-A[j])] = max(dp.get((A[i], A[i]-A[j]), 1), dp.get((A[j], A[i]-A[j]), 1)+1)
                maxLen = max(maxLen, dp[(A[i], A[i]-A[j])])
            print dp
        return maxLen
