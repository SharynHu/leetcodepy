import heapq
class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        maxHeap = [(-A[0][0], 0, 0)]
        heapq.heapify(maxHeap)
        
        visited = set()
        res = min(A[0][0], A[-1][-1])
                  
        while(maxHeap):
            curr_val, curr_i, curr_j = heapq.heappop(maxHeap)
            curr_val = -curr_val
            if (curr_i, curr_j) in visited:
                continue
            if curr_i==len(A)-1 and curr_j==len(A[0])-1:
                return res
            visited.add((curr_i,curr_j))
            res = min(curr_val,res)
            for next_i, next_j in [[curr_i-1, curr_j], [curr_i+1, curr_j], [curr_i, curr_j-1], [curr_i, curr_j+1]]:
                if 0<=next_i<len(A) and 0<=next_j<len(A[0]) and (next_i, next_j) not in visited:
                    heapq.heappush(maxHeap, (-A[next_i][next_j], next_i, next_j))
