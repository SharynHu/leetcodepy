import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = nums[:k]
        heapq.heapify(minHeap)
        
        for i in range(k, len(nums)):
            if nums[i]>minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        return minHeap[0]
