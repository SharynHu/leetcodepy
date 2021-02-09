# this is equivalent to a matrix where each row and column are ascending, find the k smallest elements (leetcode 378)
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not k:
            return []
        if not nums1 or not nums2:
            return []
        res = []
        minHeap = [[nums1[0]+nums2[0], 0,0]]
        heapq.heapify(minHeap)
        visited= set()
        
        while(k>0 and minHeap):
            curr,i,j = heapq.heappop(minHeap)
            if (i,j) in visited:
                continue
            res.append([nums1[i], nums2[j]])
            k -= 1
            visited.add((i,j))
            # add its neighbors into the heap
            for next_i, next_j in [[i+1,j],[i,j+1]]:
                if next_i<len(nums1) and next_j<len(nums2):
                    heapq.heappush(minHeap, [nums1[next_i]+nums2[next_j], next_i, next_j])
            # print minHeap
        return res
