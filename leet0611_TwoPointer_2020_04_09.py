class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)<3:
            return 0
        
        res = 0
        nums.sort()
        for k in range(2,len(nums)):
            #在nums[:k]中寻找两个数i, j使nums[i]+nums[j]>nums[k]
            i , j = 0, k-1
            while(i<j and j<k):
                if nums[i]+nums[j]<=nums[k]:
                    i += 1
                    continue
                #当前nums[i]+nums[j]>nums[k]，这时所有的nums[i:j]中间的值都满足条件
                res += j-i
                j -= 1
        return res
            
