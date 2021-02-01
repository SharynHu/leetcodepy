import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, [matrix[0][0], 0, 0])
        visited = set((0, 0))
        for i in range(k):
            curr, x, y = heapq.heappop(minHeap)
            if y+1<len(matrix[0]) and (x, y+1) not in visited:
                heapq.heappush(minHeap, [matrix[x][y+1], x, y+1])
                visited.add((x, y+1))
            if x+1<len(matrix) and (x+1, y) not in visited:
                heapq.heappush(minHeap, [matrix[x+1][y], x+1, y])
                visited.add((x+1, y))
        return curr
