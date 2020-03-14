# if we already know the number of ways to get target j using numbers nums[:i], denote it as dp[i][j].
# then 
# if nums[i] == 0, dp[i][j] = dp[i-1][j]
# else dp[i][j] = dp[i-1][j-nums[i]]+dp[i-1][j+nums[i]]

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
        if sum_ == 0:
            #all numbers are zero, the signs don't matter
            if s==0:
                return 2**len(nums)
            return 0
        
        dp = collections.defaultdict(int)
        # initialization of the dp matrix
        if nums[0] == 0:
            dp[(0, 0)] = 2
        else:
            dp[(0, nums[0])] = 1
            dp[(0, -nums[0])] = 1

        for i in range(1, len(nums)):
            for j in range(-sum_, sum_+1):
                dp[(i, j)] = dp[(i-1, j-nums[i])]+dp[(i-1, j+nums[i])]

        return dp[(len(nums)-1, s)]
