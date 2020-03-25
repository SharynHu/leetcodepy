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
        MAXDIFF = max(A)-min(A)
        if MAXDIFF==0:
            #all the numbers are the same 
            return len(A)
        
        #dp[i][j] means the maximum length for a subsequence ending with index i and has step j
        dp = [[1]*(2*MAXDIFF+1) for i in range(len(A))]
        
        maxLen = 1
        for i in range(len(A)):
            for j in range(i):
                diffIndex = A[i]-A[j]+MAXDIFF
                dp[i][diffIndex] = max(dp[i][diffIndex], dp[j][diffIndex]+1)
                maxLen = max(maxLen , dp[i][diffIndex])
        return maxLen
        
                        
