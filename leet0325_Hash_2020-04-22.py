class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum = [0]*(len(nums)+1)
        sumToIndex = collections.defaultdict(list)
        
        maxLen = 0
        sumToIndex[0].append(0)
        for i in range(1, len(nums)+1):
            preSum[i] += preSum[i-1]+nums[i-1]
            #检查preSum[i]-k是否也在map里
            if preSum[i]-k in sumToIndex:
                maxLen = max([maxLen, i-sumToIndex[preSum[i]-k][-1], i-sumToIndex[preSum[i]-k][0]])
            sumToIndex[preSum[i]].append(i)
        return maxLen
