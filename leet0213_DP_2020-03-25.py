# 考虑环的影响，首位和末位不能同时为yes。这说明至少有一个的选择是no。
# (1) 如果首位我们选择no，那么从nums[1]到nums[n-1]的选择就没有环形的首尾制约，完全就是一个198.House Robber I的问题。
# (2) 如果末位我们选择no，那么从nums[0]到nums[n-2]的选择就没有环形的首尾制约，同样也是一个198.House Robber I的问题。
# 我们将两种情况下的最优解再取最大值，就是答案。
class Solution(object):
    def helper(self, nums):
        if not nums:
            return 0
        #dp1[i] means the maximum profit we can get so far if we rob house i-1
        dp1 = [0]*(len(nums)+1)
        #dp2[i] means the maximub profit we can get so far if we do not rob house i-1
        dp2 = [0]*(len(nums)+1)
        
        for i in range(1, len(nums)+1):
            # if we want to rob house i-1
            dp1[i] = dp2[i-1]+nums[i-1]
            dp2[i] = max(dp2[i-1], dp1[i-1])
        return max(dp1[-1], dp2[-1])
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<=3:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums)-1]))
