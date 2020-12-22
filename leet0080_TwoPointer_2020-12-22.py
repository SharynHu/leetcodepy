class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        
        while(j<len(nums)):
            # make j the last but one  nums[j]
            while(j+2<len(nums) and nums[j+2]==nums[j+1] and nums[j]==nums[j+1]):
                j += 1
            # we got a j either is the last but one nums[j] or is the only nums[j]
            # if nums[j] is the only nums[j] in the array, i.e., it has no duplicates
            if j+1>=len(nums) or nums[j+1]!=nums[j]:
                nums[i] = nums[j]
                i += 1
                j += 1
                continue
            # if nums[j] is the last but one nums[j] in the array
            nums[i] = nums[j]
            i += 1
            j += 1
            nums[i] = nums[j]
            i += 1
            j += 1
        return i
