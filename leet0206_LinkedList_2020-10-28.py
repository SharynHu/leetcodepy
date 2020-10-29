# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        p = head
        q = head.next
        p.next = None
        while(q):
            next_p = q
            next_q = q.next
            q.next = p
            p = next_p
            q = next_q
        return p
        
