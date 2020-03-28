#规律
#对于index i，如果i是偶数，那么i就要比后面的数小，如果i是奇数，那么i就要比后面的数大。
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-1):
            if i%2==0:
                if nums[i]>nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            if i%2==1:
                if nums[i]<nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
