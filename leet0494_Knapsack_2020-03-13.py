# 解法二
#这题就是将nums分成正负两个集合， 使得他们的差为target
#假设正集合为P， 负集合为N,  那么我们有 sum(P)-sum(N) = target，又 sum(P)+sum(N) = sum(nums)， 那么
# sum(P)-(sum(nums)-sum(P)) = target, sum(P) = (sum(nums)+target)/2。
# 所以这道题转化为在nums中找到一个集合， 该集合的和为(sum(nums)+target)/2

class Solution(object):
    def findTargetSumWays(self, nums, s):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        sum_ = sum(nums)
        if (sum_+s)%2 != 0 or s>sum_: 
            return 0
        dp = [0]*(sum_+1)
        dp[0] = 1
        
        for i in range(len(nums)):
            for j in range(sum_, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[(sum_+s)/2]
