class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution: put nums[i] on index nums[i]-1
        i = 0
        while(i<len(nums)):
            # if the current number is in its correct position, we do nothing and move on to the next index
            if i+1==nums[i]:
                i += 1
                continue
            # else we first check if the position nums[i]-1 has the same number with nums[i]
            if nums[i] == nums[nums[i]-1]:
                return nums[i]
            else:
                # we swap the two number
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp
        # loop through the whole array to find the duplicate
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return nums[i]
