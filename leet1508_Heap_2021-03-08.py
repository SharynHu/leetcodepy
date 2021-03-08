# it is like k merge k sorted array.
# for each number in nums, if we fix the start, we will get a set of subarrays:
# [a1, a1+a2, ..., a1+a2+...+an]
# [a2, a2+a3, ..., a2+a3+...+an]
# ...
# [an]
# each subarray is sorted and we need to merge those subarrays. So we use heap.
import heapq
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        minHeap = [(nums[i], i) for i in range(n)]
        heapq.heapify(minHeap)
        
        sum_ = 0
        count = 0
        while(count<right):
            count += 1
            curr_val, curr_j = heapq.heappop(minHeap)
            if count>=left and count<=right:
                sum_ += curr_val
            if count>right:
                return sum_%(10**9+7)
            # calculate the next minimum
            if curr_j+1<n:
                heapq.heappush(minHeap, (curr_val+nums[curr_j+1], curr_j+1))
        return sum_%(10**9+7)
