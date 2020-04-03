class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        k = 0
        #all numbers before i are 0s;
        #all numbers after j are 2s
        #all numbers between i and k are ones
        #all numbers between k and j are unsorted
        while(k<=j):       
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
                continue
            if nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                continue
            #由于i和k的increasement在nums[k]=0, 2时是同步的， 因此只有在遇到nums[k]==1的时候,k会比i多增加一个
            #因此处在i和k之间的所有数都是1
            if nums[k] == 1:
                k += 1
