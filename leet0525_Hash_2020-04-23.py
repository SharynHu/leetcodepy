# 建立累加和sum，遍历所有元素，遇到1加1，遇到0减1. 如果两个位置的累加和相等，说明中间的元素和是0，即有相同数目的0和1.
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preSum = [0]*(len(nums)+1)
        sums = collections.defaultdict(list)
        sums[0].append(0)
        maxLen = 0
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                preSum[i] = preSum[i-1]-1
            else:
                preSum[i] = preSum[i-1]+1
            sums[preSum[i]].append(i)
            maxLen = max(maxLen, i-sums[preSum[i]][0])
        return maxLen
            
