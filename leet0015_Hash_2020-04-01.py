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
            hashset = set()
            for j in range(i+1,len(nums)):
                #同样需要保证j是最后一个nums[j]
                if j<len(nums)-1 and nums[j]==nums[j+1]:
                    hashset.add(nums[j])
                    continue
                if -nums[i]-nums[j] in hashset:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])
                hashset.add(nums[j])
        return res
