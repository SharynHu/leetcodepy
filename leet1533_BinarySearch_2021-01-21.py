# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l, r, x, y):
#        """
#        :type l, r, x, y: int
#        :rtype int
#        """
#
#	 # Returns the length of the array
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        presum = [0]
        left, right = 0, reader.length()-1
        while(left+1<right):
            if (right-left+1)%2==0:
                l=left
                r = (left+right)/2
                x = (left+right)/2+1
                y = right
            else:
                l = left
                r = (left+right)/2
                x = (left+right)/2
                y = right
            if reader.compareSub(l,r,x,y)>0:
                right = r
                continue
            else:
                left = x
                continue
                
        if reader.compareSub(left, left, right, right)>0:
            return left
        return right
