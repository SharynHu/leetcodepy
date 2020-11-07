
class Solution(object):
    def partition(self, low, high, nums):
        #step1:  choose nums[high] as a pivot; initialize i, and j
        pivot = nums[high]
        # elements before(including) index i are less than pivot
        i = low - 1
        # elements between i and j are bigger than pivot
        j = low
        # elements after j(including j) needs to be processed
        # less..i|bigger|j...pivot
        
        #step2: traverse the unprocessed 
        while(j<len(nums)):
            if nums[j]>=pivot:
                j += 1
                continue
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            
        #step3, put the pivot where it is
        nums[i+1], nums[high] = nums[high], nums[i+1]
        
        #step4, return the index of the pivot
        return i+1
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high, k = 0, len(nums)-1,len(nums)-k+1
        while(low<high):
            pivotIndex = self.partition(low, high, nums)
            if pivotIndex==k-1:
                return nums[pivotIndex]
            if pivotIndex<k-1:
                low = pivotIndex+1
            else:
                high = pivotIndex-1
        return nums[low]
            
