# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        q = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(n):
            q = q.next
        while(q):
            p = p.next
            q = q.next
            prev = prev.next
        prev.next = p.next
        return dummy.next
        
            
        
