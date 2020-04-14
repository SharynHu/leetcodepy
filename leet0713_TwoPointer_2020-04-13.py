class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k==0:
            return 0
        
        i = 0
        j = 0
        currProduct = 1
        res = 0
        while(j<len(nums)):
            #当前nums[i:j+1]的乘积为currProduct
            currProduct *= nums[j]
            #如果此时nums[i:j+1]的乘积大于等于k,那么我们需要将i向右移动，由于我们需要以j结尾的所有解，因此i移动的位数越少越好
            while(i<j and currProduct>=k):
                currProduct /= nums[i]
                i += 1
            #如果当前nums[i:j+1]的乘积小于k,那么对于所有i<=p<=j来说， nums[p:j+1]都满足条件，而对于所有的p<i,nums[p:j+1]的乘积大于等于k, 因此满足条件的以j结尾的subarray只有j-i+1个
            if currProduct<k:
                res += j-i+1
            #寻找下一个满足条件的解
            j +=1
        return res
                    
