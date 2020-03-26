# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        heapq.heapify(heap)
        
        dummy = ListNode(0)
        #ninitialize minheap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        
        p = dummy
        while(heap):
            currNode = heapq.heappop(heap)[1]
            if currNode.next:
                heapq.heappush(heap, (currNode.next.val, currNode.next))
            currNode.next = None
            p.next = currNode
            p = p.next
        return dummy.next
