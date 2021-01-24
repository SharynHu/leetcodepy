class Solution(object):
    def partition(self, low, high, nums):
        # choose a pivot, here it is nums[high]     
        # we set two indice i and j
        i = low-1
        j = low
        # elements before(including) i are smaller than nums[high]; elements between i and j are bigger than nums[high]; elements after(including) j are unprocessed
        
        # we traverse throught the unprocessed part
        while(j<high):
            if nums[j]>=nums[high]:
                j += 1
                continue
            else:
                # we swap it with nums[i+1]
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
                j += 1
        # swap nums[i+1] with nums[pivot]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1
        
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums)-k+1
        low = 0
        high = len(nums)-1
        
        while(low<=high):
            # calculate the position of nums[high] in the  array if it is sorted.
            pivotIndex = self.partition(low, high, nums)
            # if there are k elements smaller than or equal to nums[high], we get what we want: the k-th smallest number in nums.
            if pivotIndex+1==k:
                return nums[pivotIndex]
            # if the pivot is less than k-1, it means that we need to find a bigger nums[pivot]. We just need to search nums[pivot:high+1] because all numbers before pivot are less than numbers after(including) pivot
            if pivotIndex+1<k:
                low = pivotIndex+1
            else:
                high = pivotIndex-1
        # check left
        if self.partition(low, high, nums)==k-1:
            return high
        return low
