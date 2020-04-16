#当存在duplicates的时候，需要关注的是等号成立的地方
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        #寻找target最左边的index
        res = [-1, -1]
        left, right = 0, len(nums)-1
        while(left+1<right):
            middle = (left+right)/2
            #寻找最左边的index，因此在nums[middle]==target的时候选取最左边的区间作为target存在的可能区间
            if nums[middle]>=target:
                right = middle
                continue
            left = middle
        if nums[left] == target:
            res[0] = left
        elif nums[right] == target:
            res[0] = right
            
        #寻找target最右边的index
        left, right = 0, len(nums)-1
        while(left+1<right):
            middle = (left+right)/2
            #寻找最右边的index，因此在nums[middle]==target的时候选取最右边的区间作为target存在的可能区间
            if nums[middle]<=target:
                left = middle
                continue
            right = middle
        if nums[right] == target:
            res[1] = right
        elif nums[left] == target:
            res[1] = left
        return res
