class Solution(object):
    def atMostK(self, A, K):
        counter = collections.defaultdict(int)
        i = 0
        res = 0
        
        for j in range(len(A)):
            counter[A[j]] += 1
            while(len(counter)>K):
                counter[A[i]] -= 1
                if counter[A[i]] == 0:
                    counter.pop(A[i])
                i += 1
            if len(counter)<=K:
                res += j-i+1
                # print i, j
        return res
                
        
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A or K==0:
            return 0
        return self.atMostK(A, K)-self.atMostK(A, K-1)
