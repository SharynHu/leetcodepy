class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            preSum[i+1] = nums[i]+preSum[i]

        count = 0
        hashMap = collections.defaultdict(int)
        for i in range(len(preSum)):
            if preSum[i]-k in hashMap:
                count += hashMap[preSum[i]-k]
            hashMap[preSum[i]] += 1
        return count
