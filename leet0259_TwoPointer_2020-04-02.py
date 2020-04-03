class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums)<3:
            return 0
        
        res = 0
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                currSum = nums[i]+nums[j]+nums[k]
                if currSum>=target:
                    k -= 1
                    continue
                if currSum<target:
                    #如果j,k加起来小于target-nums[i]，那么固定j的话，所有在j, k之间的数也都满足条件
                    res+=k-j
                    j += 1
        return res
