#skip the duplicate directly
#push进去的数字比当前pop out的数字大， 而heap里存留的数字也比当前pop out的数字大， 因此， 后面pop out出来的值，永远大于等于先pop out出来的值， 因此在pop out检查duplicates时，只需要与前一个pop out出来的值进行比较

import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        minHeap = [1]
        heapq.heapify(minHeap)
        prev = 0
        i = 0
        while(i<n):
            curr = heapq.heappop(minHeap)
            if curr==prev:
                continue
            prev = curr
            i += 1
            heapq.heappush(minHeap, curr*2)
            heapq.heappush(minHeap, curr*3)
            heapq.heappush(minHeap, curr*5)
        return curr
