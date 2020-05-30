#方法二：
#该题实际上就是从nums每一列中抽取一个数，组成一个新的数列arr,要求max(arr)-min(arr)最小
#使用一个堆存放当前抽取的数，初始化为[nums[i][0] for i in range(len(nums))]， 下面要pop出堆中的最小值，在相应行取一个值（不然的话range只会越来越大）。重复该操作直到某行为空。
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        #minHeap用来保存
        minHeap = []
        for i in range(len(nums)):
            minHeap.append([nums[i][0], i])
        heapq.heapify(minHeap)
        
        #initialize start and end
        currMin, currMax= minHeap[0][0], max([nums[i][0] for i in range(len(nums))])
        start, end = currMin, currMax

        while(minHeap):
            currVal, currRow = heapq.heappop(minHeap)
            if not nums[currRow]:
                break
            newVal = nums[currRow].pop(0)
            heapq.heappush(minHeap, [newVal, currRow])
            currMin = minHeap[0][0]
            currMax= max(newVal, currMax)
            if currMax-currMin<end-start:
                start, end = currMin, currMax
        return start, end
                
               
                
