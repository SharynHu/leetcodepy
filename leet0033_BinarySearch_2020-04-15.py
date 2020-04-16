class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        left = 0
        right = len(nums)-1
        while(left+1<right):
            middle = (left+right)/2
            if nums[middle]==target:
                return middle
            #需要知道middle究竟在target的左边还是target的右边
            #假如middle在target的左边， 那么
            if nums[left]<=nums[middle]<target or target<nums[left]<nums[middle] or nums[middle]<target<=nums[right]:
                left = middle
            else:
                right = middle
                        
                
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
                    
