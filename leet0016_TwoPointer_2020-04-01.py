class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        closest = float('inf')
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                currSum = nums[i]+nums[j]+nums[k]
                # print i, j, k, currSum
                if abs(currSum-target)<abs(closest-target):
                    closest = currSum
                if currSum > target:
                    k -= 1
                    continue
                if currSum < target:
                    j += 1
                    continue
                return target
        return closest
