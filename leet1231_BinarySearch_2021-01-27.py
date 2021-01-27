# divide a array into K subarrays and get the minimum subarray sum
# the problem is to find the maximum minimum subarray sum
class Solution(object):
    def count(self, sweetness, candidate):
        container = 0
        currSum = 0
        for num in sweetness:
            #count groups that has sum than sweetness
            currSum += num
            if currSum>=candidate:
                currSum = 0
                container += 1
        return container
            
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """

        left = 0
        right = sum(sweetness)
        while(left+1<right):
            middle = (left+right)/2
            count = self.count(sweetness, middle)
            if count>=K+1:
                left = middle
            else:
                right = middle
        # check left and right
        
        if self.count(sweetness, right)>=K+1:
            return right
        return left
