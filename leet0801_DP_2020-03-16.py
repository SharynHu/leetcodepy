# sub-problem: when A[:i-1], B[:i-1] are strictly increasing after swapping, then if A[i-1]<A[i-2] and 
# B[i-1]>B[i-2], there is no need for swapping.
# key point: we do not know the value for A[i-1] and B[i-1] after swapping.
# So we need an extra denotation for this value.

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or len(A) == 1:
            return 0
        dp_swap = range(len(A)+1)
        dp_noswap = range(len(A)+1)
        dp_swap[1] = 1
        dp_noswap[1] = 0
        
        
        for i in range(2, len(A)+1):
            
            if A[i-1]>B[i-2] and B[i-1]>A[i-2]:
                dp_noswap[i] = min(dp_noswap[i], dp_swap[i-1])
                dp_swap[i] = min(dp_swap[i], dp_noswap[i-1]+1)
            if A[i-1]>A[i-2] and B[i-1]>B[i-2]:
                dp_noswap[i] = min(dp_noswap[i], dp_noswap[i-1])
                dp_swap[i] = min(dp_swap[i], dp_swap[i-1]+1)
        return min(dp_swap[-1], dp_noswap[-1])
