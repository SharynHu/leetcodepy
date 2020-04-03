class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j>(i+1) and nums[j]==nums[j-1]: 
                    continue
                # Now it is a 2sum problem
                hashset = set()
                k = j+1
                while(k<len(nums)):
                    if target-nums[i]-nums[j]-nums[k] in hashset:
                        res.append([nums[i], nums[j], nums[k], target-nums[i]-nums[j]-nums[k]])
                        #skip duplicate
                        while(k+1<len(nums) and nums[k]==nums[k+1]):
                            k += 1
                    hashset.add(nums[k])
                    k += 1
        return res
