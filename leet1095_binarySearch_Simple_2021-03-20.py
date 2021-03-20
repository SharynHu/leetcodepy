# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

# First find the index of the peak.
# Try finding target in the first part, if not found, try finging it in the second part. Both use Binary Search.

class Solution(object):
    def findPeak(self, A):
        left, right = 0, A.length()-1
        while(left+1<right):
            middle = (left+right)/2
            if A.get(middle-1)<A.get(middle) and A.get(middle)>A.get(middle+1):
                return middle
            if A.get(middle+1)>A.get(middle):
                left = middle
            else:
                right = middle
        # print left,right
        if left>=1 and A.get(left-1)<A.get(left)<A.get(left+1):
            return left
        return right
                
                
    def binarySearchLeft(self, A, start, end, target):
        left, right = start, end
        # print left, right
        while(left+1<right):
            middle = (left+right)/2
            if A.get(middle)>=target:
                right = middle
            else:
                left = middle
        if A.get(left) == target:
            return left
        if A.get(right) == target:
            return right
        return -1
    
    
    
    def binarySearchRight(self, A, start, end, target):
        left, right = start, end
        while(left+1<right):
            middle = (left+right)/2
            if A.get(middle)<=target:
                right = middle
            else:
                left = middle
        if A.get(left) == target:
            return left
        if A.get(right) == target:
            return right
        return -1
    
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        peakIndex = self.findPeak(mountain_arr)
        # print peakIndex
        index1 = self.binarySearchLeft(mountain_arr, 0, peakIndex, target)
        if index1!=-1:
            return index1
        index2 = self.binarySearchRight(mountain_arr, peakIndex, mountain_arr.length()-1, target)
        # print index2
        if index2!=-1:
            return index2
        return -1
