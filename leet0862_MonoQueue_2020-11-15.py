class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        presum = [0]
        for i in range(len(A)):
            presum.append(A[i]+presum[-1])
        print presum
        queue = collections.deque()
        minLen = float('inf')
        for i in range(len(presum)):
            # the trickest part
            # if we find presum[i]<presum[queue[-1]], it means that queue[-1] is not possible to be the start index, because presum[i] is always closer.
            while(queue and presum[i]<=presum[queue[-1]]):
                queue.pop()
            while(queue and presum[i]>=presum[queue[0]]+K):
                minLen = min(minLen, i-queue.popleft())
            queue.append(i)
        if minLen == float('inf'):
            return -1
        return minLen
