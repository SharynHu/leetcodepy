class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProduct = [1]*(len(nums)+1)
        rightProduct = [1]*(len(nums)+1)
        
        for i in range(len(nums)):
            leftProduct[i+1] = leftProduct[i]*nums[i]
            rightProduct[len(nums)-i-1] = rightProduct[len(nums)-i]*nums[len(nums)-i-1]
        output = []

        for i in range(len(nums)):
            output.append(leftProduct[i]*rightProduct[i+1])
        return output
