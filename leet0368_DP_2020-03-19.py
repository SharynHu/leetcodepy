class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        #dp[i] means the maximum subarray ending with i
        #initializtion
        dp = collections.defaultdict(list)
        dp[1] = [1]
        for num in nums:
            dp[num] = max([dp[i]+[num] for i in dp if not dp[i] or num%dp[i][-1]==0], key=len) 
                
        return max([dp[i][1:] for i in dp], key=len)
