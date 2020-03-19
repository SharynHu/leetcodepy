#我们可以将nums中所有的数字放回它原有的位置。
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            #如果当前的数字不在其该在的位置，即将其放到对应的位置
            while(0<=nums[i]-1<len(nums) and nums[nums[i]-1]!=nums[i]):
                #put it in the place it should be 
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        #check if we put all the numbers in the right place
        #the first one that is not in the right place is the missing one
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        #if all the numbers are in the right position, then it is the last number that is missing
        return len(nums)+1
