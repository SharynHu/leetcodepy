#去重，需要排序
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            #由于需要去重，需要保证i是第一个nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            #此问题转化为2sum问题，即对每个nums[i], 寻找一对j, k使得 nums[j]+nums[k] = -nums[i]
            j = i+1
            k= len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    #为j, k找到一组解
                    res.append([nums[i], nums[j], nums[k]])
                    #不再使用重复的j, k
                    while(j+1<len(nums) and nums[j]==nums[j+1]):
                        j += 1
                    while(k-1>=0 and nums[k]==nums[k-1]):
                        k -= 1
                    j += 1
                    k -= 1
                    continue
                if nums[i]+nums[j]+nums[k]>0:
                    k -= 1
                    continue
                if nums[i]+nums[j]+nums[k]<0:
                    j += 1
            
                
        return res
                    
