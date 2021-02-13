import bisect
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        # the operation only shrinks the sum of the array, so if the sum is already smaller than or equal to the target, there should be no elements in the array changed. In this case, the smallest value is the largest element in the arr.
        if sum(arr)<=target:
            return arr[-1]
        # now sum(arr)>target, we need to make it smaller.
        # the minimum sum we can get is value*len(arr) where value<=arr[0]. if arr[0]*len(arr) is still bigger than or equal to target, then value must be smaller than or equal to arr[0]. The closest one we choose is target/len(arr).
        if arr[0]*len(arr)>=target:
            # we choose the value satisfying that value<=arr[0] and abs(value*len(arr)-target) is the smallest
            candidate1 = target/len(arr)
            candidate2 = target/len(arr)+1
            if candidate2>arr[0]:
                return candidate1
            if abs(candidate2*len(arr)-target)<abs(candidate1*len(arr)-target):
                return candidate2
            return candidate1
        
        # now value is between arr[0] and arr[-1].
        preSum = [0]
        closest = arr[0]
        closestSum = arr[0]*len(arr)
        
        for i in range(len(arr)):
            preSum.append(preSum[-1]+arr[i])
        
        left, right = arr[0], arr[-1]
        while(left+1<right):
            middle = (left+right)/2
            # there are len(arr)-middle-1 that is larger than arr[middle], so now the sum actually become:
            index = bisect.bisect_left(arr, middle)
            summ = preSum[index]+middle*(len(arr)-index)
            # print middle, preSum[middle],summ
            if summ==target:
                return middle
            # check if the summ is closer
            if abs(summ-target)<abs(closestSum-target):
                closest = middle
                closestSum = summ
            # check where we search
            if summ>target:
                right = middle
            else:
                left = middle
        
        #check left and right
        index = bisect.bisect_left(arr, left)
        summ = preSum[index]+left*(len(arr)-index)
        if abs(summ-target)<abs(closestSum-target):
            closest = left
            closestSum = summ
        index = bisect.bisect_left(arr, right)
        summ = preSum[index]+right*(len(arr)-index)
        if abs(summ-target)<abs(closestSum-target):
            closest = right
            closestSum = summ
        return closest
        
                
