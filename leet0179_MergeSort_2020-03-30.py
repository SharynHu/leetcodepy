class Solution(object):
    def compare(self, num1, num2):
        a = num1*(10**len(str(num2)))+num2
        b = num2*(10**len(str(num1)))+num1
        if a<b:return -1
        if a==b:return 0
        return 1
    
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        left = self.mergeSort(nums[:len(nums)/2])
        right = self.mergeSort(nums[len(nums)/2:])
        newNums = []
        while(left and right):
            if self.compare(left[0], right[0])==-1:
                newNums.append(right.pop(0))
            else:
                newNums.append(left.pop(0))
        while(left):
            newNums.append(left.pop(0))
        while(right):
            newNums.append(right.pop(0))
        return newNums
                
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = self.mergeSort(nums)
        res =  ''.join(map(str, nums))
        #去除头部的0
        return str(int(res))
