#方法一：对所有数进行排序，找出包含k个来自不同行的最小区间（滑动窗口）。
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        minHeap = []
        sortedNums = []
        for i in range(len(nums)):
            minHeap.append([nums[i].pop(0), i])
        heapq.heapify(minHeap)
        while(minHeap):
            currVal, currRow = heapq.heappop(minHeap)
            sortedNums.append([currVal, currRow])
            if nums[currRow]:
                heapq.heappush(minHeap, [nums[currRow].pop(0), currRow])
        
        count = collections.defaultdict(int)
        i, j, k = 0, 0, len(nums)
        start, end = float('-inf'), float('inf')
        while(i<len(sortedNums) and j<len(sortedNums)):
            count[sortedNums[j][1]] += 1
            #在更新start, end时要保证nums[i][j]是valid的，所以要先更新start和end
            while(len(count)>=k):
                if sortedNums[j][0]-sortedNums[i][0]<end-start:
                    start, end = sortedNums[i][0], sortedNums[j][0]
                if sortedNums[j][0]-sortedNums[i][0]==end-start:
                    start, end = min(start, sortedNums[i][0]), min(end, sortedNums[j][0])
                #将i向右移动，寻找更小的区间
                count[sortedNums[i][1]] -= 1
                if count[sortedNums[i][1]] == 0:
                    count.pop(sortedNums[i][1])
                i += 1
                continue
            j += 1
                
        return start, end
                
